# ### Built-in deps
# ### Third-party deps
# ### Local deps
from ...config import get_app_config
from .manager import ReceitaFederalDataManager
from .version_checker import check_version_diff
from .downloader import DataDownloader
from .extractor import DataExtractor
from .selector import DataSelector
from .transformer import DataTransformer
from .populator import DBPopulator
from ...utils.yaml_readers import read_yaml_file


def run_rf_data_management(settings=get_app_config()):
    manager = ReceitaFederalDataManager()
    manager.start(settings)


def run_rf_version_check(settings=get_app_config()):
    is_diff = check_version_diff(
        settings.RECEITA_FEDERAL_DATA_MAIN_URL,
        settings.RECEITA_FEDERAL_MAIN_UPDATE_FIELD
    )
    return is_diff


def run_rf_data_download(is_diff, settings=get_app_config()):
    if is_diff:
        yaml_file = read_yaml_file(settings.FILES_TO_DOWNLOAD_CONFIG_PATH)

        downloader = DataDownloader(yaml_file)
        downloader.start(
            settings.RECEITA_FEDERAL_DATA_REPOSITORY_URL,
            settings.RECEITA_FEDERAL_DATA_TRIB_URL,
            settings.DOWNLOADS_FOLDER_PATH,
        )


def run_rf_data_extraction(settings=get_app_config()):
    extractor = DataExtractor(settings.TABLES_CHUNKSIZE)
    extractor.start(
        settings.DOWNLOADS_FOLDER_PATH,
        settings.EXTRACTS_FOLDER_PATH,
    )


def run_rf_data_selection(settings=get_app_config()):
    yaml_file = read_yaml_file(settings.FILES_TO_FILTER_CONFIG_PATH)
    cnpjs = set()
    aux_files = {}

    selector = DataSelector(
        filter_parameters=yaml_file,
        aux_files=aux_files,
        tables_chunksize=settings.TABLES_CHUNKSIZE,
    )
    selector.start(
        settings.EXTRACTS_FOLDER_PATH,
        settings.SELECTS_FOLDER_PATH,
        cnpjs,
    )


def run_rf_data_transformation(settings=get_app_config()):
    transformer = DataTransformer(settings.TABLES_CHUNKSIZE)
    transformer.start(
        settings.SELECTS_FOLDER_PATH,
        settings.TRANSFORMS_FOLDER_PATH,
    )


def run_rf_data_insertion(settings=get_app_config()):
    populator = DBPopulator(
        settings.AUX_FILES_PATH,
        settings.TABLES_CHUNKSIZE
    )
    populator.start(settings.TRANSFORMS_FOLDER_PATH)
