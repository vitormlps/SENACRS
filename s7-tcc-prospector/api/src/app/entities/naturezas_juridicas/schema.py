# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps


class NaturezasJuridicasBase(BaseModel):
    id: str
    descricao: str = Field(min_length=3)


class NaturezasJuridicasCreate(NaturezasJuridicasBase):
    pass


class NaturezasJuridicasUpdate(NaturezasJuridicasBase):
    id: str
    descricao: Optional[str] = Field(min_length=3)


class NaturezasJuridicasView(NaturezasJuridicasBase):
    id: str
    descricao: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
