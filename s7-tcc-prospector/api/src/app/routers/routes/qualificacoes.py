# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.qualificacoes.repository import qualificacoes_repo, QualificacoesView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["Qualificacoes"], prefix="/qualificacoes")


@router.get("", response_model=List[QualificacoesView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = qualificacoes_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Qualificacoes not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = qualificacoes_repo().count()

    if result is None:
        raise HTTPException(404, "Qualificacoes not found")

    return result


@router.get("/{id}", response_model=QualificacoesView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = qualificacoes_repo().get(id)

    if result is None:
        raise HTTPException(404, "Qualificacao not found")

    return result
