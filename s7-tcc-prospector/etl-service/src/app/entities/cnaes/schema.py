# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps


class CNAEsBase(BaseModel):
    id: str
    descricao: str = Field(min_length=3)


class CNAEsCreate(CNAEsBase):
    pass


class CNAEsUpdate(CNAEsBase):
    id: str
    descricao: Optional[str] = Field(min_length=3)


class CNAEsView(CNAEsBase):
    id: str
    descricao: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
