# ### Built-in deps
from typing import Optional
from datetime import datetime
from uuid import UUID

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps


class MunicipiosBase(BaseModel):
    codigo: str
    descricao: str = Field(min_length=3)


class MunicipiosCreate(MunicipiosBase):
    pass


class MunicipiosUpdate(MunicipiosBase):
    id: UUID
    codigo: Optional[str]
    descricao: Optional[str] = Field(min_length=3)


class MunicipiosView(MunicipiosBase):
    id: UUID
    descricao: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
