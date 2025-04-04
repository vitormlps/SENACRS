# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps
from ..base.schema import DefaultQueryFilter


class FGTSBase(BaseModel):
    tipo_devedor: str
    uf_devedor: str
    unidade_responsavel: str
    entidade_responsavel: str
    unidade_inscricao: str
    numero_inscricao: str
    tipo_situacao_inscricao: str
    situacao_inscricao: str
    receita_principal: str
    data_inscricao: datetime
    indicador_ajuizado: bool
    valor_consolidado: float


class FGTSCreate(FGTSBase):
    pass


class FGTSUpdate(FGTSBase):
    id: str
    tipo_devedor: Optional[str]
    uf_devedor: Optional[str]
    unidade_responsavel: Optional[str]
    entidade_responsavel: Optional[str]
    unidade_inscricao: Optional[str]
    numero_inscricao: Optional[str]
    tipo_situacao_inscricao: Optional[str]
    situacao_inscricao: Optional[str]
    receita_principal: Optional[str]
    data_inscricao: Optional[datetime]
    indicador_ajuizado: Optional[bool]
    valor_consolidado: Optional[float]


class FGTSView(FGTSBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class FGTSFilter(DefaultQueryFilter):
    tipo_devedor: Optional[str]
    uf_devedor: Optional[str]
    unidade_responsavel: Optional[str]
    entidade_responsavel: Optional[str]
    unidade_inscricao: Optional[str]
    numero_inscricao: Optional[str]
    tipo_situacao_inscricao: Optional[str]
    situacao_inscricao: Optional[str]
    receita_principal: Optional[str]
    data_inscricao: Optional[datetime]
    indicador_ajuizado: Optional[bool]
    valor_consolidado: Optional[float]
