# ### Built-in deps
from typing import Optional, List, Annotated
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field
from fastapi import Query

# ### Local deps
from ..base.schema import DefaultQueryFilter


class EmpresasBase(BaseModel):
    razao_social: str = Field(min_length=3)
    capital_social: float
    porte_empresa: str
    natureza_juridica: str
    qualificacao_responsavel: str


class EmpresasCreate(EmpresasBase):
    pass


class EmpresasUpdate(EmpresasBase):
    id: str
    razao_social: Optional[str] = Field(min_length=3)
    capital_social: Optional[float]
    porte_empresa: Optional[str]
    natureza_juridica: Optional[str]
    qualificacao_responsavel: Optional[str]


class EmpresasView(EmpresasBase):
    id: str
    razao_social: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class EmpresasMainView(BaseModel):
    id: str
    cnpj: str
    razao_social: str
    nome_fantasia: str
    capital_social: float
    natureza_juridica: str
    cnae: str
    cnaes_secundarios: str
    porte_empresa: str
    situacao_cadastral: str
    motivo: str
    qualificacao: str
    municipio: str
    data_opcao_simples: Optional[datetime]
    data_exclusao_simples: Optional[datetime]

    class Config:
        orm_mode = True


class EmpresasFilter(DefaultQueryFilter):
    id: Optional[str]
    razao_social: Optional[str]
    cnae: Annotated[Optional[List[str]], Query()]
    situacao_cadastral: Annotated[Optional[List[str]], Query()]
    natureza_juridica: Annotated[Optional[List[str]], Query()]
    porte_empresa: Annotated[Optional[List[str]], Query()]
    min_capital_social: Optional[float] = 0
    max_capital_social: Optional[float] = 0
