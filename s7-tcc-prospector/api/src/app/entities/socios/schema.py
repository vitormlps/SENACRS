# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps
from ..base.schema import DefaultQueryFilter


class SociosBase(BaseModel):
    cnpj_base: str = Field(min_length=8, max_length=14)
    nome: str = Field(min_length=3)
    cpf_cnpj: Optional[str] = Field(min_length=8, max_length=14)
    data_entrada_sociedade: datetime
    qualificacao: str
    pais: str
    representante_legal: str
    faixa_etaria: str


class SociosCreate(SociosBase):
    pass


class SociosUpdate(SociosBase):
    id: str
    cnpj_base: Optional[str] = Field(min_length=8, max_length=14)
    nome: Optional[str] = Field(min_length=3)
    cpf_cnpj: Optional[str] = Field(min_length=8, max_length=14)
    data_entrada_sociedade: Optional[datetime]
    qualificacao: Optional[str]
    pais: Optional[str]
    representante_legal: Optional[str]
    faixa_etaria: Optional[str]


class SociosView(SociosBase):
    id: str
    cnpj_base: Optional[str]
    nome: Optional[str]
    cpf_cnpj: Optional[str]
    data_entrada_sociedade: Optional[datetime]
    qualificacao: Optional[str]
    pais: Optional[str]
    representante_legal: Optional[str]
    faixa_etaria: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class SociosFilter(DefaultQueryFilter):
    cnpj_base: Optional[str]
    nome: Optional[str]
    cpf_cnpj: Optional[str]
    data_entrada_sociedade: Optional[datetime]
    qualificacao: Optional[str]
    pais: Optional[str]
    representante_legal: Optional[str]
    faixa_etaria: Optional[str]
