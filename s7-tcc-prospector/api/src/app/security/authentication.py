# ### Built-in deps
from typing import Dict
from uuid import uuid4
from datetime import datetime

# ### Third-party deps
import bcrypt

# ### Local deps


def check_psw(password: str, hash: str):
    return bcrypt.checkpw(password.encode(), hash.encode())


def encrypt_psw(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


class AuthManager:
    users_tokens: Dict[str, Dict[str, str | datetime]] = {}

    @staticmethod
    def set_user_token(user_id: str, token: str, origin: str):
        AuthManager.users_tokens[token] = {
            'user_id': user_id,
            'ip': origin,
            'time': datetime.now()
        }

    @staticmethod
    def generate_token():
        return str(uuid4())
