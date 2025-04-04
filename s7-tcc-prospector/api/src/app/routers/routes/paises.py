# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.paises.repository import paises_repo, PaisesView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["Paises"], prefix="/paises")


@router.get("", response_model=List[PaisesView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = paises_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Paises not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = paises_repo().count()

    if result is None:
        raise HTTPException(404, "Paises not found")

    return result


@router.get("/{id}", response_model=PaisesView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = paises_repo().get(id)

    if result is None:
        raise HTTPException(404, "Pais not found")

    return result
