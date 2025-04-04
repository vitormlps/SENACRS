# ### Built-in deps
# ### Third-party deps
# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import SIDA
from .schema import SIDAView, SIDACreate, SIDAUpdate, SIDAFilter


class SIDARepo(BaseRepo[SIDA, SIDACreate, SIDAUpdate]):
    pass


def sida_repo():
    return SIDARepo(SIDA)
