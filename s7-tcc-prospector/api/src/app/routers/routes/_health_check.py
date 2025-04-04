# ### Built-in deps
# ### Third-party deps
from fastapi import APIRouter, Depends

# ### Local deps
from ...security.current_user_auth import validate_token, validate_password
from ...entities.versionamentos.repository import versionamentos_repo
from ...entities.base.repository import reset_db
from ...entities.base.schema import Auth


router = APIRouter(tags=["Health Check"], prefix="")


@router.get("/", response_model=str)
def health_check(current_user_id: str = Depends(validate_token)):
    return "Server is running"


@router.post("/rdb", response_model=str)
def rdb(payload: Auth, current_user_id: str = Depends(validate_token)):

    psw_is_invalid = validate_password(payload.psw)
    if psw_is_invalid: return "Não autorizado"

    repo = versionamentos_repo()

    result = repo.get_versao_rf()
    reset_db()
    repo.insert_versao_rf(result)

    return "Reset successfull"
