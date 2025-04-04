# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.faixas_etarias.repository import faixas_etarias_repo, FaixasEtariasView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["FaixasEtarias"], prefix="/faixas-etarias")


@router.get("", response_model=List[FaixasEtariasView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = faixas_etarias_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Faixas etarias not found")

    return result


@router.get("/{id}", response_model=FaixasEtariasView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = faixas_etarias_repo().get(id)

    if result is None:
        raise HTTPException(404, "Faixa etaria not found")

    return result
