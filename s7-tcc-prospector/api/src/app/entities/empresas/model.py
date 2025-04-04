# ### Built-in deps
# ### Third-party deps
from sqlalchemy.orm import Mapped, mapped_column

# ### Local deps
from ..base.model import Base


class Empresa(Base):
    razao_social: Mapped[str] = mapped_column(nullable=False)
    capital_social: Mapped[float] = mapped_column(nullable=False)
    natureza_juridica: Mapped[str] = mapped_column(nullable=False)
    qualificacao_responsavel: Mapped[str] = mapped_column(nullable=False)
    porte_empresa: Mapped[str] = mapped_column(nullable=False)
