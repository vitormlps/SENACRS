# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.situacoes_cadastrais.repository import situacoes_cadastrais_repo, SituacoesCadastraisView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["SituacoesCadastrais"], prefix="/situacoes-cadastrais")


@router.get("", response_model=List[SituacoesCadastraisView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = situacoes_cadastrais_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Situacoes cadastrais not found")

    result = [item for item in result if item.descricao != "-"]

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = situacoes_cadastrais_repo().count()

    if result is None:
        raise HTTPException(404, "Situacoes cadastrais not found")

    return result


@router.get("/{id}", response_model=SituacoesCadastraisView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = situacoes_cadastrais_repo().get(id)

    if result is None:
        raise HTTPException(404, "Situacao cadastral not found")

    return result
