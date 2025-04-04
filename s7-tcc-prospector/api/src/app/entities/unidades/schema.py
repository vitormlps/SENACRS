# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps


class UnidadesBase(BaseModel):
    descricao: str


class UnidadesCreate(UnidadesBase):
    pass


class UnidadesUpdate(UnidadesBase):
    id: str
    descricao: Optional[str]


class UnidadesView(UnidadesBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
