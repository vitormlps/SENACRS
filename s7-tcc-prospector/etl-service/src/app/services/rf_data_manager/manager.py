# ### Built-in deps
from datetime import datetime, timezone, timedelta

# ### Third-party deps
import requests

# ### Local deps
from app.helpers import Logger
from app.entities.versionamentos.repository import versionamentos_repo
from .downloader import DataDownloader
from .extractor import DataExtractor
from .selector import DataSelector
from .transformer import DataTransformer
from .populator import DBPopulator
from app.utils.yaml_readers import read_yaml_file
from app.utils.files_manip import clean_folder


class ReceitaFederalDataManager:
    def __init__(self) -> None:
        self._logger = Logger().get_logger()
        self._logger.debug("Initializing ReceitaFederalDataManager")

        self.cnpjs = set()
        self.aux_files = {}

    def check_version_diff(self, rf_main_url, update_field_name):
        """
        Verifica a data da última de modificação realizada no repositório da receita federal
        """
        self._logger.info(
            "Checking if there's any update from Receita Federal")

        response = None
        try:
            response = requests.get(rf_main_url)
        except Exception as err:
            self._logger.warning(
                "Error occured while trying to connect to Receita Federal")
            self._logger.debug(err)

        if response is None or response.status_code > 399:
            self._logger.warning("Couldn't connect to Receita Federal")
            return False

        rf_updated_date = response.json()[update_field_name]
        self._logger.debug(f"Date from RF: {rf_updated_date}")

        repo = versionamentos_repo()
        result = repo.get_all_by({"skip": 0, "limit": 0})

        if result is None or len(result) == 0:
            now = datetime.now(timezone(-timedelta(hours=3))
                               ).strftime('%d/%m/%Y %H:%M:%S')
            repo.create(
                {"rf_last_update": now},
                commit=False
            )
            repo.session.commit()
            self._logger.info(
                f"No last update found. Created new RF update: {now}")
            return True

        self._logger.debug(f"Date from DB: {result[0].rf_last_update}")

        if result[0].rf_last_update != rf_updated_date:
            repo.update(
                result[0].id,
                {"rf_last_update": rf_updated_date},
                commit=False
            )
            repo.session.commit()
            self._logger.info(
                f"Last update: {result[0].rf_last_update} | RF new update: {rf_updated_date}")
            return True

        self._logger.warning("No updates from Receita Federal")
        return False

    def start(self, settings):
        self._logger.debug("Starting ReceitaFederalDataManager")

        is_diff = self.check_version_diff(
            settings.RECEITA_FEDERAL_DATA_MAIN_URL,
            settings.RECEITA_FEDERAL_MAIN_UPDATE_FIELD
        )
        has_downloaded = False

        if is_diff or settings.FORCE_DOWNLOAD:
            yaml_file = read_yaml_file(settings.FILES_TO_DOWNLOAD_CONFIG_PATH)

            downloader = DataDownloader(yaml_file)
            downloader.start(
                settings.RECEITA_FEDERAL_DATA_REPOSITORY_URL,
                settings.RECEITA_FEDERAL_DATA_TRIB_URL,
                settings.DOWNLOADS_FOLDER_PATH,
            )
            has_downloaded = True

        if has_downloaded or settings.EXTRACT_DATA:
            extractor = DataExtractor(settings.TABLES_CHUNKSIZE)
            extractor.start(
                settings.DOWNLOADS_FOLDER_PATH,
                settings.EXTRACTS_FOLDER_PATH,
            )
            clean_folder(settings.DOWNLOADS_FOLDER_PATH)

        if settings.FILTER_DATA:
            yaml_file = read_yaml_file(settings.FILES_TO_FILTER_CONFIG_PATH)

            selector = DataSelector(
                filter_parameters=yaml_file,
                aux_files=self.aux_files,
                tables_chunksize=settings.TABLES_CHUNKSIZE,
            )
            selector.start(
                settings.EXTRACTS_FOLDER_PATH,
                settings.SELECTS_FOLDER_PATH,
                self.cnpjs,
            )

        if settings.TRANSFORM_DATA:
            transformer = DataTransformer(settings.TABLES_CHUNKSIZE)
            transformer.start(
                settings.SELECTS_FOLDER_PATH,
                settings.TRANSFORMS_FOLDER_PATH,
            )

        if settings.POPULATE_DB:
            populator = DBPopulator(
                settings.AUX_FILES_PATH, settings.TABLES_CHUNKSIZE)
            populator.start(
                settings.TRANSFORMS_FOLDER_PATH,
                settings.RESET_DB
            )

        self._logger.info("Terminating ETL process")
