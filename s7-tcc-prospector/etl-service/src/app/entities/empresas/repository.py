# ### Built-in deps
import pandas as pd

# ### Third-party deps
# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Empresa
from .schema import EmpresasView, EmpresasCreate, EmpresasUpdate, EmpresasFilter, EmpresasMainView


class EmpresasRepo(BaseRepo[Empresa, EmpresasCreate, EmpresasUpdate]):

    def sql_to_dataframe(self, data):
        return pd.DataFrame(data)


def empresas_repo():
    return EmpresasRepo(Empresa)
