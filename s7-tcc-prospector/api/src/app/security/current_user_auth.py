# ### Built-in deps
from typing import Annotated

# ### Third-party deps
from fastapi import HTTPException, Header

# ### Local deps
from ..config import get_app_config
from .authentication import AuthManager


def validate_password(password: str) -> bool:
    return password != get_app_config().X_KEY


def validate_token(authorization: Annotated[str, Header()], origin: Annotated[str, Header()]):
    user_data = AuthManager.users_tokens.get(
        authorization.replace('Bearer ', '')
    )

    if user_data is None or \
            user_data['ip'] != origin:
        raise HTTPException(401, 'Token inválido')

    return user_data['user_id']


def get_current_user():
    pass


def get_current_user_admin():
    pass
