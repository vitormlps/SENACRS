# ### Built-in deps
# ### Third-party deps
# ### Local deps
from ...security.authentication import AuthManager, encrypt_psw, check_psw
from ...entities.base.repository import BaseRepo
from .model import Usuario
from .schema import UsuariosView, UsuariosCreate, UsuariosUpdate, Login


class UsuariosRepo(BaseRepo[Usuario, UsuariosCreate, UsuariosUpdate]):
    def login(self, email: str, sent_password: str, origin: str):
        user = self.get_by({'email': email, 'skip': 0, 'limit': 0})

        if user is None:
            return 'Usuário não encontrado'

        if check_psw(sent_password, user.password):
            user.token = AuthManager.generate_token()
            AuthManager.set_user_token(user.id, user.token, origin)

            return user
        
        return 'Senha inválida'


    def register(self, payload: UsuariosCreate):
        user = self.get_by({'email': payload.email, 'skip': 0, 'limit': 0})

        if user:
            return 'E-mail já registrado'

        payload.password = encrypt_psw(payload.password)
        return self.create(payload.dict())


    def update(self, id: str, payload: UsuariosUpdate):
        if payload.password:
            payload.password = encrypt_psw(payload.password)
        
        return super().update(id, payload)


def usuarios_repo():
    return UsuariosRepo(Usuario)
