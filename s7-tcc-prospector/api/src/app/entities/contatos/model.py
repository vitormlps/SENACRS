# ### Built-in deps
# ### Third-party deps
from sqlalchemy.orm import Mapped, mapped_column

# ### Local deps
from ..base.model import Base


class Contato(Base):
    tipo: Mapped[str] = mapped_column(nullable=False)
    descricao: Mapped[str] = mapped_column(nullable=False)
    estabelecimento: Mapped[str] = mapped_column(nullable=False)
