# ### Built-in deps
# ### Third-party deps
# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Pais
from .schema import PaisesView, PaisesCreate, PaisesUpdate


class PaisesRepo(BaseRepo[Pais, PaisesCreate, PaisesUpdate]):
    pass


def paises_repo():
    return PaisesRepo(Pais)
