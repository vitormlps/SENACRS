# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps
from ..base.schema import DefaultQueryFilter


class RepresentantesLegaisBase(BaseModel):
    cpf: str = Field(min_length=8, max_length=8)
    nome: str = Field(min_length=3)
    qualificacao: str


class RepresentantesLegaisCreate(RepresentantesLegaisBase):
    pass


class RepresentantesLegaisUpdate(RepresentantesLegaisBase):
    id: str
    cpf: Optional[str] = Field(min_length=8, max_length=8)
    nome: Optional[str] = Field(min_length=3)
    qualificacao: Optional[str]


class RepresentantesLegaisView(RepresentantesLegaisBase):
    id: str
    cpf: str
    nome: str
    qualificacao: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class RepresentantesLegaisFilter(DefaultQueryFilter):
    cpf: Optional[str]
    nome: Optional[str]
    qualificacao: Optional[str]
