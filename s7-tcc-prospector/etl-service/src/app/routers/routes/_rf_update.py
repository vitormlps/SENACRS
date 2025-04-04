# ### Built-in deps
# ### Third-party deps
from fastapi import APIRouter, BackgroundTasks

# ### Local deps
from ...security.auth import validate_password
from ...entities.base.schema import Auth, FilesUpdate, RFDownload
from ...services.rf_data_manager.run import (
    run_rf_data_management,
    run_rf_version_check,
    run_rf_data_download,
    run_rf_data_extraction,
    run_rf_data_selection,
    run_rf_data_transformation,
    run_rf_data_insertion
)
from ...services.update_config_files import update_config_files


router = APIRouter(tags=["Receita Federal Data Update"], prefix="/rf-update")


@router.post("/full", response_model=str)
def rf_data_update(payload: Auth, background_tasks: BackgroundTasks):
    psw_is_invalid = validate_password(payload.psw)
    if psw_is_invalid:
        return "Not authorized"

    background_tasks.add_task(
        run_rf_data_management
    )

    return "RF data update was triggered"


@router.post("/check-version", response_model=str)
def rf_version_check(payload: Auth):

    psw_is_invalid = validate_password(payload.psw)
    if psw_is_invalid:
        return "Não autorizado"

    is_diff = run_rf_version_check()
    return is_diff


@router.post("/files", response_model=str)
def update_configs(payload: FilesUpdate):

    psw_is_invalid = validate_password(payload.psw)
    if psw_is_invalid:
        return "Não autorizado"

    result = update_config_files(payload)
    return result


@router.post("/download", response_model=str)
def rf_data_download(payload: RFDownload, background_tasks: BackgroundTasks):

    psw_is_invalid = validate_password(payload.psw)
    if psw_is_invalid:
        return "Não autorizado"

    background_tasks.add_task(
        run_rf_data_download,
        is_diff=payload.is_diff
    )

    return "Download dos dados da Receita Federal foi iniciada"


@router.post("/extraction", response_model=str)
def rf_data_extraction(payload: Auth, background_tasks: BackgroundTasks):

    psw_is_invalid = validate_password(payload.psw)
    if psw_is_invalid:
        return "Não autorizado"

    background_tasks.add_task(run_rf_data_extraction)

    return "Extração dos dados da Receita Federal foi iniciada"


@router.post("/selection", response_model=str)
def rf_data_selection(payload: Auth, background_tasks: BackgroundTasks):

    psw_is_invalid = validate_password(payload.psw)
    if psw_is_invalid:
        return "Não autorizado"

    background_tasks.add_task(run_rf_data_selection)

    return "Seleção dos dados foi iniciada"


@router.post("/transformation", response_model=str)
def rf_data_transformation(payload: Auth, background_tasks: BackgroundTasks):

    psw_is_invalid = validate_password(payload.psw)
    if psw_is_invalid:
        return "Não autorizado"

    background_tasks.add_task(run_rf_data_transformation)

    return "Tranformação dos dados foi iniciada"


@router.post("/insertion", response_model=str)
def rf_data_insertion(payload: Auth, background_tasks: BackgroundTasks):

    psw_is_invalid = validate_password(payload.psw)
    if psw_is_invalid:
        return "Não autorizado"

    background_tasks.add_task(run_rf_data_insertion)

    return "Inserção dos dados foi iniciada"
