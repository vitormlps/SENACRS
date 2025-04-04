# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps
from ..base.schema import DefaultQueryFilter


class ContatosBase(BaseModel):
    tipo: str = Field(min_length=3)
    descricao: str = Field(min_length=3)
    estabelecimento: str


class ContatosCreate(ContatosBase):
    pass


class ContatosUpdate(ContatosBase):
    id: str
    tipo: Optional[str] = Field(min_length=3)
    descricao: Optional[str] = Field(min_length=3)
    estabelecimento: Optional[str]


class ContatosView(ContatosBase):
    id: str
    tipo: str
    descricao: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ContatosFilter(DefaultQueryFilter):
    tipo: Optional[str]
    descricao: Optional[str]
    estabelecimento: Optional[str]
