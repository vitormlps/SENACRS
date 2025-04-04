# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps
from ..base.schema import DefaultQueryFilter


class LogradourosBase(BaseModel):
    tipo: str = Field(min_length=3)
    nome: str = Field(min_length=3)
    numero: Optional[str] = Field(min_length=1)
    complemento: Optional[str] = Field(min_length=1)
    bairro: Optional[str] = Field(min_length=3)
    cep: str = Field(min_length=8, max_length=8)
    uf: str = Field(min_length=2, max_length=2)
    municipio: str
    nome_cidade_exterior: str
    pais: str


class LogradourosCreate(LogradourosBase):
    pass


class LogradourosUpdate(LogradourosBase):
    id: str
    tipo: Optional[str] = Field(min_length=3)
    nome: Optional[str] = Field(min_length=3)
    cep: Optional[str] = Field(min_length=8, max_length=8)
    uf: Optional[str] = Field(min_length=2, max_length=2)
    municipio: Optional[str]
    nome_cidade_exterior: Optional[str]
    pais: Optional[str]


class LogradourosView(LogradourosBase):
    id: str
    tipo: str
    nome: str
    numero: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    cep: str
    uf: str
    municipio: str
    nome_cidade_exterior: Optional[str]
    pais: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class LogradourosFilter(DefaultQueryFilter):
    tipo: Optional[str]
    nome: Optional[str]
    numero: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    cep: Optional[str]
    uf: Optional[str]
    municipio: Optional[str]
    nome_cidade_exterior: Optional[str]
    pais: Optional[str]
