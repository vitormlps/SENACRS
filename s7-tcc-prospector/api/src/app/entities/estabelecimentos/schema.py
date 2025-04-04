# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps
from ..base.schema import DefaultQueryFilter


class EstabelecimentosBase(BaseModel):
    cnpj_base: str = Field(min_length=8, max_length=8)
    cnpj_ordem: str = Field(min_length=4, max_length=4)
    cnpj_digit_verif: str = Field(min_length=2, max_length=2)
    nome_fantasia: Optional[str] = Field(min_length=3)
    data_situacao_cadastral: datetime
    data_inicio_atividade: datetime
    cnaes_secundarios: Optional[str]
    situacao_especial: Optional[str]
    data_situacao_especial: Optional[datetime]
    cnae_principal: str
    matriz_filial: str
    situacao_cadastral: str
    motivo: str
    logradouro: str


class EstabelecimentosCreate(EstabelecimentosBase):
    pass


class EstabelecimentosUpdate(EstabelecimentosBase):
    id: str
    cnpj_base: Optional[str] = Field(min_length=8, max_length=8)
    cnpj_ordem: Optional[str] = Field(min_length=4, max_length=4)
    cnpj_digit_verif: Optional[str] = Field(min_length=2, max_length=2)
    data_situacao_cadastral: Optional[datetime]
    data_inicio_atividade: Optional[datetime]
    cnae_principal: Optional[str]
    matriz_filial: Optional[str]
    situacao_cadastral: Optional[str]
    motivo: Optional[str]
    logradouro: Optional[str]


class EstabelecimentosView(EstabelecimentosBase):
    id: str
    cnpj_base: str
    cnpj_ordem: str
    cnpj_digit_verif: str
    nome_fantasia: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class EstabelecimentosFilter(DefaultQueryFilter):
    cnpj_base: Optional[str]
    cnpj_ordem: Optional[str]
    cnpj_digit_verif: Optional[str]
    data_situacao_cadastral: Optional[datetime]
    data_inicio_atividade: Optional[datetime]
    empresa_cnpj: Optional[str]
    cnae_principal: Optional[str]
    matriz_filial: Optional[str]
    situacao_cadastral: Optional[str]
    motivo: Optional[str]
    logradouro: Optional[str]
