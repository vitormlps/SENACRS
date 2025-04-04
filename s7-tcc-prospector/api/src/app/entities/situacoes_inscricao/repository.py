# ### Built-in deps
# ### Third-party deps

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import SituacaoInscricao
from .schema import SituacoesInscricaoView, SituacoesInscricaoCreate, SituacoesInscricaoUpdate


class SituacoesInscricaoRepo(BaseRepo[SituacaoInscricao, SituacoesInscricaoCreate, SituacoesInscricaoUpdate]):
    pass


def situacoes_inscricao_repo():
    return SituacoesInscricaoRepo(SituacaoInscricao)
