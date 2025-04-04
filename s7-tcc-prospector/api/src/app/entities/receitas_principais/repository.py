# ### Built-in deps
# ### Third-party deps

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import ReceitaPrincipal
from .schema import ReceitasPrincipaisView, ReceitasPrincipaisCreate, ReceitasPrincipaisUpdate


class ReceitasPrincipaisRepo(BaseRepo[ReceitaPrincipal, ReceitasPrincipaisCreate, ReceitasPrincipaisUpdate]):
    pass


def receitas_principais_repo():
    return ReceitasPrincipaisRepo(ReceitaPrincipal)
