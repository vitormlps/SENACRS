# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.logradouros.repository import logradouros_repo, LogradourosView, LogradourosFilter


router = APIRouter(tags=["Logradouros"], prefix="/logradouros")


@router.get("", response_model=List[LogradourosView])
def get_all_by(
        query: LogradourosFilter = Depends(LogradourosFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = logradouros_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Logradouros not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = logradouros_repo().count()

    if result is None:
        raise HTTPException(404, "Logradouros not found")

    return result

@router.get("/estados")
def get():
    result = logradouros_repo().get_estados()

    if result is None:
        raise HTTPException(404, "Estados not found")

    return result


@router.get("/{id}", response_model=LogradourosView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = logradouros_repo().get(id)

    if result is None:
        raise HTTPException(404, "Logradouro not found")

    return result
