# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps


class PortesEmpresasBase(BaseModel):
    descricao: str = Field(min_length=3)


class PortesEmpresasCreate(PortesEmpresasBase):
    pass


class PortesEmpresasUpdate(PortesEmpresasBase):
    id: str
    descricao: Optional[str] = Field(min_length=3)


class PortesEmpresasView(PortesEmpresasBase):
    id: str
    descricao: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
