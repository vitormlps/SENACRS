# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps


class ReceitasPrincipaisBase(BaseModel):
    descricao: str


class ReceitasPrincipaisCreate(ReceitasPrincipaisBase):
    pass


class ReceitasPrincipaisUpdate(ReceitasPrincipaisBase):
    id: str
    descricao: Optional[str]


class ReceitasPrincipaisView(ReceitasPrincipaisBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
