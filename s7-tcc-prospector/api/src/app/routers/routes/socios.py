# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.socios.repository import socios_repo, SociosView, SociosFilter


router = APIRouter(tags=["Socios"], prefix="/socios")


@router.get("", response_model=List[SociosView])
def get_all_by(
        query: SociosFilter = Depends(SociosFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = socios_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Socios not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = socios_repo().count()

    if result is None:
        raise HTTPException(404, "Socios not found")

    return result


@router.get("/{id}", response_model=SociosView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = socios_repo().get(id)

    if result is None:
        raise HTTPException(404, "Socio not found")

    return result
