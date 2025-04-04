# ### Built-in deps
from datetime import datetime

# ### Third-party deps
from sqlalchemy.orm import Mapped, mapped_column

# ### Local deps
from ..base.model import Base


class Simples(Base):
    data_opcao: Mapped[datetime] = mapped_column(nullable=True)
    data_exclusao: Mapped[datetime] = mapped_column(nullable=True)
