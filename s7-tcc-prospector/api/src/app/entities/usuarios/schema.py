# ### Built-in deps
from typing import Optional

# ### Third-party deps
from pydantic import BaseModel, Field, EmailStr

# ### Local deps


class Login(BaseModel):
    email: str
    psw: str


class UsuariosBase(BaseModel):
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=2)
    email: EmailStr
    password: str = Field(min_length=8)


class UsuariosCreate(UsuariosBase):
    pass


class UsuariosUpdate(UsuariosBase):
    id: str
    first_name: Optional[str] = Field(min_length=3)
    last_name: Optional[str] = Field(min_length=2)
    email: Optional[EmailStr]
    password: Optional[str] = Field(min_length=8)


class UsuariosView(UsuariosBase):
    id: str
    token: Optional[str]

    def dict(self, **kwargs):
        kwargs['exclude'] = {'password'}
        return super().dict(**kwargs)

    def json(self, **kwargs):
        kwargs['exclude'] = {'password'}
        return super().json(**kwargs)

    class Config:
        orm_mode = True
