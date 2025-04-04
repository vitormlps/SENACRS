# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.portes_empresas.repository import portes_empresas_repo, PortesEmpresasView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["PortesEmpresas"], prefix="/portes-empresas")


@router.get("", response_model=List[PortesEmpresasView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = portes_empresas_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Portes empresas not found")

    return result


@router.get("/{id}", response_model=PortesEmpresasView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = portes_empresas_repo().get(id)

    if result is None:
        raise HTTPException(404, "Porte empresa not found")

    return result
