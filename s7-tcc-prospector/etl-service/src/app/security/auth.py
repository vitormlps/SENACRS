# ### Built-in deps
# ### Third-party deps
# ### Local deps
from ..config import get_app_config


def validate_password(password: str) -> bool:
    return password != get_app_config().X_KEY
