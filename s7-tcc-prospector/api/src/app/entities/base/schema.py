# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps


class DefaultQueryFilter(BaseModel):
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    skip: Optional[int] = 0
    limit: Optional[int] = 0


class BaseFilter(DefaultQueryFilter):
    codigo: Optional[str]
    descricao: Optional[str]


class Auth(BaseModel):
    psw: Optional[str]
