# ### Built-in deps
# ### Third-party deps

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import TipoSituacaoInscricao
from .schema import TiposSituacaoInscricaoView, TiposSituacaoInscricaoCreate, TiposSituacaoInscricaoUpdate


class TiposSituacaoInscricaoRepo(BaseRepo[TipoSituacaoInscricao, TiposSituacaoInscricaoCreate, TiposSituacaoInscricaoUpdate]):
    pass


def tipos_situacao_inscricao_repo():
    return TiposSituacaoInscricaoRepo(TipoSituacaoInscricao)
