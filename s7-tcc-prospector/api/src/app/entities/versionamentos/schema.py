# ### Built-in deps
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps


class VersionamentosBase(BaseModel):
    rf_last_update: str = Field(min_length=19, max_length=19)


class VersionamentosCreate(VersionamentosBase):
    pass


class VersionamentosUpdate(VersionamentosBase):
    id: str
    rf_last_update: str = Field(min_length=19, max_length=19)


class VersionamentosView(VersionamentosBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
