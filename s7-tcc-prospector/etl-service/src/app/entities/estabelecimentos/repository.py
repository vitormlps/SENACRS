# ### Built-in deps
# ### Third-party deps
from sqlalchemy import select

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Estabelecimento
from .schema import EstabelecimentosView, EstabelecimentosCreate, EstabelecimentosUpdate, EstabelecimentosFilter


class EstabelecimentosRepo(BaseRepo[Estabelecimento, EstabelecimentosCreate, EstabelecimentosUpdate]):
    def get_all_cnpjs(self):
        query = select(self.model.cnpj_base)
        results = self.session.execute(query).all()
        return results


def estabelecimentos_repo():
    return EstabelecimentosRepo(Estabelecimento)
