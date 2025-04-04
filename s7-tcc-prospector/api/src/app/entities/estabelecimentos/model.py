# ### Built-in deps
from datetime import datetime

# ### Third-party deps
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

# ### Local deps
from ..base.model import Base


class Estabelecimento(Base):
    cnpj_base: Mapped[str] = mapped_column(String(8), nullable=False)
    cnpj_ordem: Mapped[str] = mapped_column(String(4), nullable=False)
    cnpj_digit_verif: Mapped[str] = mapped_column(String(2), nullable=False)
    nome_fantasia: Mapped[str] = mapped_column(nullable=True)
    data_situacao_cadastral: Mapped[datetime] = mapped_column(nullable=False)
    data_inicio_atividade: Mapped[datetime] = mapped_column(nullable=False)
    cnaes_secundarios: Mapped[str] = mapped_column(nullable=True)
    situacao_especial: Mapped[str] = mapped_column(nullable=True)
    data_situacao_especial: Mapped[datetime] = mapped_column(nullable=True)

    matriz_filial: Mapped[str] = mapped_column(nullable=False)
    situacao_cadastral: Mapped[str] = mapped_column(nullable=False)
    motivo: Mapped[str] = mapped_column(nullable=False)
    cnae_principal: Mapped[str] = mapped_column(nullable=False)
    logradouro: Mapped[str] = mapped_column(nullable=False)
