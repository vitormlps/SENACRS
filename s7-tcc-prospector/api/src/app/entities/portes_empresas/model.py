# ### Built-in deps
# ### Third-party deps
from sqlalchemy.orm import Mapped, mapped_column

# ### Local deps
from ..base.model import Base


class PorteEmpresa(Base):
    descricao: Mapped[str] = mapped_column(nullable=False)
