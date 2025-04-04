# ### Built-in deps
# ### Third-party deps
# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import CNAE
from .schema import CNAEsView, CNAEsCreate, CNAEsUpdate


class CNAEsRepo(BaseRepo[CNAE, CNAEsCreate, CNAEsUpdate]):
    pass


def cnaes_repo():
    return CNAEsRepo(CNAE)
