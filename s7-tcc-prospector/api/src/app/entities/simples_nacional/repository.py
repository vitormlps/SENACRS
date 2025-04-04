# ### Built-in deps
from typing import List, Dict

# ### Third-party deps
from pydantic import BaseModel
from sqlalchemy import select, delete

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Simples
from ..empresas.model import Empresa
from .schema import SimplesView, SimplesCreate, SimplesUpdate, SimplesFilter


class SimplesRepo(BaseRepo[Simples, SimplesCreate, SimplesUpdate]):
    def get_all_not_in_empresa(self, filters: BaseModel) -> List[Simples]:
        filters: Dict = filters.dict()

        query = select(self.model.id).except_(select(Empresa.id))

        if filters["skip"] != 0:
            query = query.offset(filters["skip"])

        if filters["limit"] != 0:
            query = query.limit(filters["limit"])

        results = self.session.execute(query).all()
        results = [result[0] for result in results]

        print("Diferença simples pra empresa:", len(results))
        self.session.close()

        self.bulk_delete(results)

    def bulk_delete(self, ids):
        query = delete(self.model).where(self.model.id.in_(ids))
        result = self.execute_transaction(query)
        print(result)


def simples_nacional_repo():
    return SimplesRepo(Simples)
