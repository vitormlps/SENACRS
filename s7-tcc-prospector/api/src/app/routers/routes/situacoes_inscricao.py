# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.situacoes_inscricao.repository import situacoes_inscricao_repo, SituacoesInscricaoView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["Situacoes Inscricao"], prefix="/situacoes_inscricao")


@router.get("", response_model=List[SituacoesInscricaoView])
def get_all_by(
    query: BaseFilter = Depends(BaseFilter),
    current_user_id: str = Depends(validate_token),
):
    result = situacoes_inscricao_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Situacoes Inscricao not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = situacoes_inscricao_repo().count()

    if result is None:
        raise HTTPException(404, "Situacoes Inscricao not found")

    return result


@router.get("/{id}", response_model=SituacoesInscricaoView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = situacoes_inscricao_repo().get(id)

    if result is None:
        raise HTTPException(404, "Situacao Inscricao not found")

    return result
