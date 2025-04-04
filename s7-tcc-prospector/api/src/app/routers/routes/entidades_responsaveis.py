# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.entidades_responsaveis.repository import entidades_responsaveis_repo, EntidadesResponsaveisView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["Entidades Responsaveis"], prefix="/entidades_responsaveis")


@router.get("", response_model=List[EntidadesResponsaveisView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = entidades_responsaveis_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Entidades Responsaveis not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = entidades_responsaveis_repo().count()

    if result is None:
        raise HTTPException(404, "Entidades Responsaveis not found")

    return result


@router.get("/{id}", response_model=EntidadesResponsaveisView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = entidades_responsaveis_repo().get(id)

    if result is None:
        raise HTTPException(404, "Entidade Responsavel not found")

    return result
