# ### Built-in deps
# ### Third-party deps
# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Representante
from .schema import RepresentantesLegaisView, RepresentantesLegaisCreate, RepresentantesLegaisUpdate, RepresentantesLegaisFilter


class RepresentantesLegaisRepo(BaseRepo[Representante, RepresentantesLegaisCreate, RepresentantesLegaisUpdate]):
    pass


def representantes_legais_repo():
    return RepresentantesLegaisRepo(Representante)
