from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Pessoa(Base):
    __tablename__ = 'pessoa'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    senha: Mapped[str] = mapped_column(String(50), nullable=False)

class Pessoa2(Base):
    __tablename__ = 'pessoa2'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    senha: Mapped[str] = mapped_column(String(50), nullable=False)
    idade: Mapped[int] = mapped_column(Integer)
