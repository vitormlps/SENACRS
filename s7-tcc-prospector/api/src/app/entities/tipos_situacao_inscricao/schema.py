# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps


class TiposSituacaoInscricaoBase(BaseModel):
    descricao: str


class TiposSituacaoInscricaoCreate(TiposSituacaoInscricaoBase):
    pass


class TiposSituacaoInscricaoUpdate(TiposSituacaoInscricaoBase):
    id: str
    descricao: Optional[str]


class TiposSituacaoInscricaoView(TiposSituacaoInscricaoBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
