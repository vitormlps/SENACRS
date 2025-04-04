# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.simples_nacional.repository import simples_nacional_repo, SimplesView, SimplesFilter


router = APIRouter(tags=["Simples"], prefix="/simples-nacional")


@router.get("", response_model=List[SimplesView])
def get_all_by(
        query: SimplesFilter = Depends(SimplesFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = simples_nacional_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Simples nacional not found")

    return result

@router.get("/not_in")
def get_all_not_in_empresa(
        query: SimplesFilter = Depends(SimplesFilter),
        current_user_id: str = Depends(validate_token),
    ):
    simples_nacional_repo().get_all_not_in_empresa(filters=query)


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = simples_nacional_repo().count()

    if result is None:
        raise HTTPException(404, "Simples nacional not found")

    return result


@router.get("/{id}", response_model=SimplesView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = simples_nacional_repo().get(id)

    if result is None:
        raise HTTPException(404, "Simples nacional not found")

    return result
