# ### Built-in deps
# ### Third-party deps
# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Previdenciario
from .schema import PrevidenciarioView, PrevidenciarioCreate, PrevidenciarioUpdate, PrevidenciarioFilter


class PrevidenciarioRepo(BaseRepo[Previdenciario, PrevidenciarioCreate, PrevidenciarioUpdate]):
    pass


def previdenciario_repo():
    return PrevidenciarioRepo(Previdenciario)
