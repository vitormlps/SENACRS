# ### Built-in deps
from typing import Optional, List, Annotated
from datetime import datetime, date

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
    natureza_juridica: str
    cnae: str
    porte_empresa: str
    municipio: str
    data_opcao_simples: Optional[date]

    class Config:
        orm_mode = True


class EmpresasTribView(BaseModel):
    id: str
    cnpj: str
    razao_social: str
    natureza_juridica: str
    cnae: str
    municipio: str
    fgts: str
    sida: str
    prev: str

    class Config:
        orm_mode = True


class EmpresasFilter(DefaultQueryFilter):
    cnae: Annotated[Optional[List[str]], Query()]
    situacao_cadastral: Annotated[Optional[List[str]], Query()]
    natureza_juridica: Annotated[Optional[List[str]], Query()]
    porte_empresa: Annotated[Optional[List[str]], Query()]
    municipio: Annotated[Optional[List[str]], Query()]
    uf: Annotated[Optional[List[str]], Query()]
    situacao_especial: Optional[bool]
    min_capital_social: Optional[float] = 0
    max_capital_social: Optional[float] = 0

    tipo_trib: Optional[str]
    situacao_inscricao: Annotated[Optional[List[str]], Query()]
    tipo_situacao_inscricao: Annotated[Optional[List[str]], Query()]
    tipo_devedor: Annotated[Optional[List[str]], Query()]
    tipo_credito: Annotated[Optional[List[str]], Query()]
    entidade_responsavel: Annotated[Optional[List[str]], Query()]
    unidade_responsavel: Annotated[Optional[List[str]], Query()]
    unidade_inscricao: Annotated[Optional[List[str]], Query()]
    receita_principal: Annotated[Optional[List[str]], Query()]
    indicador_ajuizado: Optional[bool]
    min_valor_consolidado: Optional[float] = 0
    max_valor_consolidado: Optional[float] = 0


class XKey(BaseModel):
    psw: Optional[str]
