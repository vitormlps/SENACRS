# ### Built-in deps
from typing import List

# ### Third-party deps
from sqlalchemy import select

# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Logradouro
from ..municipios.model import Municipio
from .schema import LogradourosView, LogradourosCreate, LogradourosUpdate, LogradourosFilter


class LogradourosRepo(BaseRepo[Logradouro, LogradourosCreate, LogradourosUpdate]):

    def get_estados(self) -> List[str]:
        query = select(
            self.model.uf,
            self.model.municipio,
            Municipio.descricao
        ).join(
            Municipio, self.model.municipio == Municipio.id, isouter=True
        ).distinct()

        data = []
        try:
            data = self.session.execute(query).all()
        except Exception as err:
            print(err)

        self.session.close()

        result = {}
        for item in data:
            estado = item[0]
            munic_id = item[1]
            municipio = item[2]

            temp_uf = result.get(estado)
            if temp_uf is None:
                result[estado] = [{
                    'id': munic_id,
                    'descricao': municipio
                }]
            else:
                result[estado].append({
                    'id': munic_id,
                    'descricao': municipio
                })

        return result


def logradouros_repo():
    return LogradourosRepo(Logradouro)
