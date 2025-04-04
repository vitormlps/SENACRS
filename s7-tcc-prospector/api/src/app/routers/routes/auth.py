# ### Built-in deps
from typing import Annotated

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException, Header

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.usuarios.repository import usuarios_repo, Login, UsuariosCreate, UsuariosUpdate, UsuariosView


router = APIRouter(tags=['Authentication'], prefix='/auth')


@router.post('', response_model=UsuariosView)
def login(payload: Login, origin: Annotated[str, Header()]):
    result = usuarios_repo().login(payload.email, payload.psw, origin)

    if isinstance(result, str):
        raise HTTPException(400, result)
    
    return result


@router.get('/user/{id}', response_model=UsuariosView)
def get(id: str, current_user_id: str = Depends(validate_token)):
    result = usuarios_repo().get(id)

    if result is None:
        raise HTTPException(404, 'Usuário não encontrado')

    return result


@router.post('/user', response_model=UsuariosView)
def register(payload: UsuariosCreate):
    result = usuarios_repo().register(payload)

    if isinstance(result, str):
        raise HTTPException(400, result)

    if result is None:
        raise HTTPException(500, 'Não foi possível registrar o usuário')

    return result

@router.put('/user/{id}', response_model=UsuariosView)
def update(
    id: str, 
    payload: UsuariosUpdate, 
    current_user_id: str = Depends(validate_token)
):
    result = usuarios_repo().update(id, payload)

    if result is None:
        raise HTTPException(500, 'Não foi possível atualizar o usuário')

    return result


@router.delete('/user/{id}', response_model=UsuariosView)
def delete(id: str, current_user_id: str = Depends(validate_token)):
    result = usuarios_repo().remove(id)

    if result is None:
        raise HTTPException(500, 'Não foi possível remover o usuário')

    return 'Usuário removido com sucesso'
