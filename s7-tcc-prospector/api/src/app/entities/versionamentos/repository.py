# ### Built-in deps
from datetime import datetime, timezone, timedelta

# ### Third-party deps
# ### Local deps
from ...entities.base.repository import BaseRepo
from .model import Versionamento
from .schema import VersionamentosView, VersionamentosCreate, VersionamentosUpdate


class VersionamentosRepo(BaseRepo[Versionamento, VersionamentosCreate, VersionamentosUpdate]):
    def get_versao_rf(self):
        result = self.get_all_by({
            "id": None,
            "created_at": None,
            "updated_at": None,
            "skip": 0,
            "limit": 0,
        })

        if result and len(result) > 0:
            result = result[0].rf_last_update
            return result

    def insert_versao_rf(self, result):
        if result:
            result = self.create({"rf_last_update": result})
        else:
            result = self.create({
                "rf_last_update": datetime.now(timezone(-timedelta(hours=3))).strftime('%d/%m/%Y %H:%M:%S')
            })


def versionamentos_repo():
    return VersionamentosRepo(Versionamento)
