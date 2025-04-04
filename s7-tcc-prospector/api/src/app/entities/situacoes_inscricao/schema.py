# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps


class SituacoesInscricaoBase(BaseModel):
    descricao: str


class SituacoesInscricaoCreate(SituacoesInscricaoBase):
    pass


class SituacoesInscricaoUpdate(SituacoesInscricaoBase):
    id: str
    descricao: Optional[str]


class SituacoesInscricaoView(SituacoesInscricaoBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
