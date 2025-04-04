# ### Built-in deps
# ### Third-party deps

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import TipoCredito
from .schema import TiposCreditoView, TiposCreditoCreate, TiposCreditoUpdate


class TiposCreditoRepo(BaseRepo[TipoCredito, TiposCreditoCreate, TiposCreditoUpdate]):
    pass


def tipos_credito_repo():
    return TiposCreditoRepo(TipoCredito)
