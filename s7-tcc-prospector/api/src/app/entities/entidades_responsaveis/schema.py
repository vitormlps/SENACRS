# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps


class EntidadesResponsaveisBase(BaseModel):
    descricao: str


class EntidadesResponsaveisCreate(EntidadesResponsaveisBase):
    pass


class EntidadesResponsaveisUpdate(EntidadesResponsaveisBase):
    id: str
    descricao: Optional[str]


class EntidadesResponsaveisView(EntidadesResponsaveisBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
