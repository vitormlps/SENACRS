# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.receitas_principais.repository import receitas_principais_repo, ReceitasPrincipaisView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["Receitas Principais"], prefix="/receitas_principais")


@router.get("", response_model=List[ReceitasPrincipaisView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = receitas_principais_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Receitas Principais not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = receitas_principais_repo().count()

    if result is None:
        raise HTTPException(404, "Receitas Principais not found")

    return result


@router.get("/{id}", response_model=ReceitasPrincipaisView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = receitas_principais_repo().get(id)

    if result is None:
        raise HTTPException(404, "Receita Principal not found")

    return result
