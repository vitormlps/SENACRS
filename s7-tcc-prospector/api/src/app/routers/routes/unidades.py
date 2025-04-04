# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.unidades.repository import unidades_repo, UnidadesView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["Unidades"], prefix="/unidades")


@router.get("", response_model=List[UnidadesView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = unidades_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Unidades not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = unidades_repo().count()

    if result is None:
        raise HTTPException(404, "Unidades not found")

    return result


@router.get("/{id}", response_model=UnidadesView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = unidades_repo().get(id)

    if result is None:
        raise HTTPException(404, "Unidade not found")

    return result
