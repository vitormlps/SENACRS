# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps


class TiposCreditoBase(BaseModel):
    descricao: str


class TiposCreditoCreate(TiposCreditoBase):
    pass


class TiposCreditoUpdate(TiposCreditoBase):
    id: str
    descricao: Optional[str]


class TiposCreditoView(TiposCreditoBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
