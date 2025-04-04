# ### Built-in deps
from datetime import datetime

# ### Third-party deps
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

# ### Local deps
from ..base.model import Base


class Socio(Base):
    cnpj_base: Mapped[str] = mapped_column(String(8), nullable=False)
    nome: Mapped[str] = mapped_column(nullable=False)
    cpf_cnpj: Mapped[str] = mapped_column(nullable=True)
    data_entrada_sociedade: Mapped[datetime] = mapped_column(nullable=False)
    qualificacao: Mapped[str] = mapped_column(nullable=True)
    pais: Mapped[str] = mapped_column(nullable=True)
    representante_legal: Mapped[str] = mapped_column(nullable=True)
    faixa_etaria: Mapped[str] = mapped_column(nullable=True)
