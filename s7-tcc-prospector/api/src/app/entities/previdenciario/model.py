# ### Built-in deps
from datetime import datetime

# ### Third-party deps
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

# ### Local deps
from ..base.model import Base


class Previdenciario(Base):
    cnpj_base: Mapped[str] = mapped_column(String(8), nullable=False)
    tipo_devedor: Mapped[str] = mapped_column(nullable=False)
    uf_devedor: Mapped[str] = mapped_column(nullable=False)
    unidade_responsavel: Mapped[str] = mapped_column(nullable=False)
    numero_inscricao: Mapped[str] = mapped_column(nullable=False)
    tipo_situacao_inscricao: Mapped[str] = mapped_column(nullable=False)
    situacao_inscricao: Mapped[str] = mapped_column(nullable=False)
    tipo_credito: Mapped[str] = mapped_column(nullable=False)
    data_inscricao: Mapped[datetime] = mapped_column(nullable=False)
    indicador_ajuizado: Mapped[bool] = mapped_column(nullable=False)
    valor_consolidado: Mapped[float] = mapped_column(nullable=False)
