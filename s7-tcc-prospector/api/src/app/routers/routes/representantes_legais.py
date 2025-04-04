# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.representantes_legais.repository import representantes_legais_repo, RepresentantesLegaisView, RepresentantesLegaisFilter


router = APIRouter(tags=["RepresentantesLegais"], prefix="/representantes-legais")


@router.get("", response_model=List[RepresentantesLegaisView])
def get_all_by(
        query: RepresentantesLegaisFilter = Depends(RepresentantesLegaisFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = representantes_legais_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Representantes legais not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = representantes_legais_repo().count()

    if result is None:
        raise HTTPException(404, "Representantes legais not found")

    return result


@router.get("/{id}", response_model=RepresentantesLegaisView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = representantes_legais_repo().get(id)

    if result is None:
        raise HTTPException(404, "Representante legal not found")

    return result
