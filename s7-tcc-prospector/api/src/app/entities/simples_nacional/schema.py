# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel

# ### Local deps
from ..base.schema import DefaultQueryFilter


class SimplesBase(BaseModel):
    data_opcao: datetime
    data_exclusao: Optional[datetime]


class SimplesCreate(SimplesBase):
    pass


class SimplesUpdate(SimplesBase):
    id: str
    data_opcao: Optional[datetime]
    data_exclusao: Optional[datetime]


class SimplesView(SimplesBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class SimplesFilter(DefaultQueryFilter):
    data_opcao: Optional[datetime]
    data_exclusao: Optional[datetime]
