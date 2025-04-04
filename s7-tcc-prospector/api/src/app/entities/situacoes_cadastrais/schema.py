# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps


class SituacoesCadastraisBase(BaseModel):
    descricao: str = Field(min_length=3)


class SituacoesCadastraisCreate(SituacoesCadastraisBase):
    pass


class SituacoesCadastraisUpdate(SituacoesCadastraisBase):
    id: str
    descricao: Optional[str] = Field(min_length=3)


class SituacoesCadastraisView(SituacoesCadastraisBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
