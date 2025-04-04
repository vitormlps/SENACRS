# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.tipos_devedor.repository import tipos_devedor_repo, TiposDevedorView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["Tipos Devedor"], prefix="/tipos_devedor")


@router.get("", response_model=List[TiposDevedorView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = tipos_devedor_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Tipos Devedor not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = tipos_devedor_repo().count()

    if result is None:
        raise HTTPException(404, "Tipos Devedor not found")

    return result


@router.get("/{id}", response_model=TiposDevedorView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = tipos_devedor_repo().get(id)

    if result is None:
        raise HTTPException(404, "Tipo Devedor not found")

    return result
