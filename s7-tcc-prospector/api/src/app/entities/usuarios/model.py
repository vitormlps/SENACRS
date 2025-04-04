# ### Built-in deps
# ### Third-party deps
from sqlalchemy.orm import relationship, Mapped, mapped_column

# ### Local deps
from ..base.model import Base


class Usuario(Base):
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
