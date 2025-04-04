# ### Built-in deps
# ### Third-party deps
from sqlalchemy.orm import Mapped, mapped_column

# ### Local deps
from ..base.model import Base


class Logradouro(Base):
    tipo: Mapped[str] = mapped_column(nullable=False)
    nome: Mapped[str] = mapped_column(nullable=False)
    numero: Mapped[str] = mapped_column(nullable=True)
    complemento: Mapped[str] = mapped_column(nullable=True)
    bairro: Mapped[str] = mapped_column(nullable=True)
    cep: Mapped[str] = mapped_column(nullable=False)
    uf: Mapped[str] = mapped_column(nullable=False)
    municipio: Mapped[str] = mapped_column(nullable=False)
    nome_cidade_exterior: Mapped[str] = mapped_column(nullable=False)
    pais: Mapped[str] = mapped_column(nullable=False)
