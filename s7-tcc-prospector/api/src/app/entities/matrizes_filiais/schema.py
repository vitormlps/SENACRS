#!/usr/bin/env python3

# ### Built-in deps
from typing import Optional
from datetime import datetime

# ### Third-party deps
from pydantic import BaseModel, Field

# ### Local deps


class MatrizesFiliaisBase(BaseModel):
    descricao: str = Field(min_length=3)


class MatrizesFiliaisCreate(MatrizesFiliaisBase):
    pass


class MatrizesFiliaisUpdate(MatrizesFiliaisBase):
    id: str
    descricao: Optional[str] = Field(min_length=3)


class MatrizesFiliaisView(MatrizesFiliaisBase):
    id: str
    descricao: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
