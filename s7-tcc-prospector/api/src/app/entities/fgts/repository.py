# ### Built-in deps
# ### Third-party deps
# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import FGTS
from .schema import FGTSView, FGTSCreate, FGTSUpdate, FGTSFilter


class FGTSRepo(BaseRepo[FGTS, FGTSCreate, FGTSUpdate]):
    pass


def fgts_repo():
    return FGTSRepo(FGTS)
