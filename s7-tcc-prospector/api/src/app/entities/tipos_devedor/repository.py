# ### Built-in deps
# ### Third-party deps

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import TipoDevedor
from .schema import TiposDevedorView, TiposDevedorCreate, TiposDevedorUpdate


class TiposDevedorRepo(BaseRepo[TipoDevedor, TiposDevedorCreate, TiposDevedorUpdate]):
    pass


def tipos_devedor_repo():
    return TiposDevedorRepo(TipoDevedor)
