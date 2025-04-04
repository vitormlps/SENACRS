# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.contatos.repository import contatos_repo, ContatosView, ContatosFilter


router = APIRouter(tags=["Contatos"], prefix="/contatos")


@router.get("", response_model=List[ContatosView])
def get_all_by(
        query: ContatosFilter = Depends(ContatosFilter),
        current_user_id: str = Depends(validate_token),
    ):
    result = contatos_repo().get_all_by(filters=query)

    if result is None or len(result) == 0:
        raise HTTPException(404, "Contatos not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = contatos_repo().count()

    if result is None:
        raise HTTPException(404, "Contatos not found")

    return result


@router.get("/{id}", response_model=ContatosView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = contatos_repo().get(id)

    if result is None:
        raise HTTPException(404, "Contato not found")

    return result
