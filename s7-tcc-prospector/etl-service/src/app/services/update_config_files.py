# ### Built-in deps
from typing import List

# ### Third-party deps
import yaml

# ### Local deps
from app.helpers import Logger
from ..config import get_app_config
from ..entities.base.schema import FilesUpdate


def update_config_files(payload: FilesUpdate, settings=get_app_config()):
    _logger = Logger().get_logger()
    _logger.debug("Starting update on config files")

    result = "Arquivos e filtros já estão com esta configuração"
    if payload.files is None and payload.filters is None:
        _logger.warning("Nothing to update")
        return result

    result = ""
    if len(payload.files) > 0:
        result = update_files(payload.files, settings, _logger)
        result += " | "

    if len(payload.filters) > 0:
        result += update_filters(payload.filters, settings, _logger)

    return result


def update_files(files: List, settings, _logger) -> str:
    _logger.debug("Updating files to process")

    result = "Arquivos já estão com esta configuração"
    with open(settings.FILES_TO_DOWNLOAD_CONFIG_PATH) as dl_config_file:
        yaml_file = yaml.load(dl_config_file, Loader=yaml.FullLoader)

        if yaml_file['files'] == files:
            _logger.warning("Nothing to update on files to process")
            return result

        is_saved = save_yaml_file(
            {"files": files},
            settings.FILES_TO_DOWNLOAD_CONFIG_PATH,
            _logger
        )

        result = "Arquivos foram atualizados" if is_saved else "Erro ao atualizar os arquivos"
        return result


def update_filters(filters, settings, _logger) -> str:
    _logger.debug("Updating filters to process")

    result = "Filtros já estão com esta configuração"
    with open(settings.FILES_TO_FILTER_CONFIG_PATH) as filters_config_file:
        yaml_file = yaml.load(filters_config_file, Loader=yaml.FullLoader)

        if yaml_file == filters:
            _logger.warning("Nothing to update on filters to process")
            return result

        is_saved = save_yaml_file(
            filters,
            settings.FILES_TO_FILTER_CONFIG_PATH,
            _logger
        )

        result = "Filtros foram atualizados" if is_saved else "Erro ao atualizar os filtros"
        return result


def save_yaml_file(file: List, file_path: str, _logger) -> bool:
    _logger.debug("Saving updates on files/filters to process")

    is_saved = True
    try:
        with open(file_path, "w") as file_to_save:
            file_to_save.write(
                yaml.dump(
                    file,
                    default_flow_style=True,
                    default_style='"'
                )
            )
    except Exception as err:
        _logger.error(err)
        is_saved = False

    return is_saved
