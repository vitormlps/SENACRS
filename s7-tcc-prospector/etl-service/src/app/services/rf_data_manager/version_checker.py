# ### Built-in deps
from datetime import datetime, timezone, timedelta

# ### Third-party deps
import requests

# ### Local deps
from app.helpers import Logger
from app.entities.versionamentos.repository import versionamentos_repo


def check_version_diff(rf_main_url, update_field_name) -> str:
    """
    Verifica a data da última de modificação realizada no repositório da receita federal
    """
    _logger = Logger().get_logger()
    _logger.info("Checking if there's any update from Receita Federal")

    response = None
    try:
        response = requests.get(rf_main_url)
    except Exception as err:
        _logger.error(
            "Error occured while trying to connect to Receita Federal")
        _logger.debug(err)

    if response is None or response.status_code > 399:
        _logger.warning("Couldn't connect to Receita Federal")
        return "Não foi possível conectar com a Receita Federal"

    rf_updated_date = response.json()[update_field_name]
    _logger.debug(f"Date from RF: {rf_updated_date}")

    repo = versionamentos_repo()
    result = repo.get_all_by({"skip": 0, "limit": 0})

    now = datetime.now(timezone(-timedelta(hours=3))
                       ).strftime('%d/%m/%Y %H:%M:%S')

    if result is None or len(result) == 0:
        repo.create({"rf_last_update": now}, commit=False)
        repo.session.commit()

        _logger.warning(f"No last update found. Created new RF update: {now}")
        return f"Data da última atualização não encontrada. Nova data registrada: {now}"

    _logger.debug(f"Date from DB: {result[0].rf_last_update}")

    if result[0].rf_last_update != rf_updated_date:
        repo.update(
            result[0].id,
            {"rf_last_update": rf_updated_date},
            commit=False
        )
        repo.session.commit()
        _logger.info(
            f"Last update: {result[0].rf_last_update} | RF new update: {rf_updated_date}")
        return f"Data da última atualização: {result[0].rf_last_update}. Nova data registrada: {now}"

    _logger.info("No updates from Receita Federal")
    return "Não há nova atualização da Receita Federal"
