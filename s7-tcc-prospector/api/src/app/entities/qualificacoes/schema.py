# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps


class QualificacoesBase(BaseModel):
    descricao: str = Field(min_length=3)


class QualificacoesCreate(QualificacoesBase):
    pass


class QualificacoesUpdate(QualificacoesBase):
    id: str
    descricao: Optional[str] = Field(min_length=3)


class QualificacoesView(QualificacoesBase):
    id: str
    descricao: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
