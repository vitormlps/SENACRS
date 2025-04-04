# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.matrizes_filiais.repository import matrizes_filiais_repo, MatrizesFiliaisView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["MatrizesFiliais"], prefix="/matriz-filiais")


@router.get("", response_model=List[MatrizesFiliaisView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = matrizes_filiais_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Matrizes filiais not found")

    return result


@router.get("/{id}", response_model=MatrizesFiliaisView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = matrizes_filiais_repo().get(id)

    if result is None:
        raise HTTPException(404, "Matriz filial not found")

    return result
