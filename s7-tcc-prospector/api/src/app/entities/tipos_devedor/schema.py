# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps


class TiposDevedorBase(BaseModel):
    descricao: str


class TiposDevedorCreate(TiposDevedorBase):
    pass


class TiposDevedorUpdate(TiposDevedorBase):
    id: str
    descricao: Optional[str]


class TiposDevedorView(TiposDevedorBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
