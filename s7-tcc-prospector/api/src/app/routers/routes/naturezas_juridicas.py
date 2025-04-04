# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.naturezas_juridicas.repository import naturezas_juridicas_repo, NaturezasJuridicasView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["NaturezasJuridicas"], prefix="/naturezas-juridicas")


@router.get("", response_model=List[NaturezasJuridicasView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = naturezas_juridicas_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Naturezas juridicas not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = naturezas_juridicas_repo().count()

    if result is None:
        raise HTTPException(404, "Naturezas juridicas not found")

    return result


@router.get("/{id}", response_model=NaturezasJuridicasView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = naturezas_juridicas_repo().get(id)

    if result is None:
        raise HTTPException(404, "Natureza juridica not found")

    return result
