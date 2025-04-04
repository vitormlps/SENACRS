# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps
from ..base.schema import DefaultQueryFilter


class PrevidenciarioBase(BaseModel):
    tipo_devedor: str
    uf_devedor: str
    unidade_responsavel: str
    numero_inscricao: str
    tipo_situacao_inscricao: str
    situacao_inscricao: str
    tipo_credito: str
    data_inscricao: datetime
    indicador_ajuizado: bool
    valor_consolidado: float


class PrevidenciarioCreate(PrevidenciarioBase):
    pass


class PrevidenciarioUpdate(PrevidenciarioBase):
    id: str
    tipo_devedor: Optional[str]
    uf_devedor: Optional[str]
    unidade_responsavel: Optional[str]
    numero_inscricao: Optional[str]
    tipo_situacao_inscricao: Optional[str]
    situacao_inscricao: Optional[str]
    tipo_credito: Optional[str]
    data_inscricao: Optional[datetime]
    indicador_ajuizado: Optional[bool]
    valor_consolidado: Optional[float]


class PrevidenciarioView(PrevidenciarioBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PrevidenciarioFilter(DefaultQueryFilter):
    tipo_devedor: Optional[str]
    uf_devedor: Optional[str]
    unidade_responsavel: Optional[str]
    numero_inscricao: Optional[str]
    tipo_situacao_inscricao: Optional[str]
    situacao_inscricao: Optional[str]
    tipo_credito: Optional[str]
    data_inscricao: Optional[datetime]
    indicador_ajuizado: Optional[bool]
    valor_consolidado: Optional[float]
