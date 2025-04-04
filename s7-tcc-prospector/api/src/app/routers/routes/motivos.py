# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.motivos.repository import motivos_repo, MotivosView
from ...entities.base.schema import BaseFilter


router = APIRouter(tags=["Motivos"], prefix="/motivos")


@router.get("", response_model=List[MotivosView])
def get_all_by(
        query: BaseFilter = Depends(BaseFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = motivos_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Motivos not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = motivos_repo().count()

    if result is None:
        raise HTTPException(404, "Motivos not found")

    return result


@router.get("/{id}", response_model=MotivosView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = motivos_repo().get(id)

    if result is None:
        raise HTTPException(404, "Motivo not found")

    return result
