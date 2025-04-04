# ### Built-in deps
# ### Third-party deps

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Unidade
from .schema import UnidadesView, UnidadesCreate, UnidadesUpdate


class UnidadesRepo(BaseRepo[Unidade, UnidadesCreate, UnidadesUpdate]):
    pass


def unidades_repo():
    return UnidadesRepo(Unidade)
