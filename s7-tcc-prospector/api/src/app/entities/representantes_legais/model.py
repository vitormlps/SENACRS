# ### Built-in deps
# ### Third-party deps
from sqlalchemy.orm import Mapped, mapped_column

# ### Local deps
from ..base.model import Base


class Representante(Base):
    cpf: Mapped[str] = mapped_column(nullable=False, index=True)
    nome: Mapped[str] = mapped_column(nullable=False)

    qualificacao: Mapped[str] = mapped_column(nullable=False)
