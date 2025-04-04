# ### Built-in deps
# ### Third-party deps

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import EntidadeResponsavel
from .schema import EntidadesResponsaveisView, EntidadesResponsaveisCreate, EntidadesResponsaveisUpdate


class EntidadesResponsaveisRepo(BaseRepo[EntidadeResponsavel, EntidadesResponsaveisCreate, EntidadesResponsaveisUpdate]):
    pass


def entidades_responsaveis_repo():
    return EntidadesResponsaveisRepo(EntidadeResponsavel)
