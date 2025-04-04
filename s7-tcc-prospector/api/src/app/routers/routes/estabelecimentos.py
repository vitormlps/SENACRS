# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.estabelecimentos.repository import estabelecimentos_repo, EstabelecimentosView, EstabelecimentosFilter


router = APIRouter(tags=["Estabelecimentos"], prefix="/estabelecimentos")


@router.get("", response_model=List[EstabelecimentosView])
def get_all_by(
        query: EstabelecimentosFilter = Depends(EstabelecimentosFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = estabelecimentos_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Estabelecimentos not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = estabelecimentos_repo().count()

    if result is None:
        raise HTTPException(404, "Estabelecimentos not found")

    return result


@router.get("/{id}", response_model=EstabelecimentosView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = estabelecimentos_repo().get(id)

    if result is None:
        raise HTTPException(404, "Estabelecimento not found")

    return result
