from sqlalchemy import ForeignKey, create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class time(Base):
    __tablename__ = "tabela_time"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    numero_camisa: Mapped[int] = mapped_column(Integer)
    posição: Mapped[str] = mapped_column(String(250))

class jogador(Base):
    __tablename__ = "tabela_jogador"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    numero_camisa: Mapped[int] = mapped_column(Integer)
    posição: Mapped[str] = mapped_column(String(250))
        
    time_id: Mapped[int] = mapped_column(ForeignKey("tabela_time.id"))
    Time: Mapped["time"] = relationship(back_populates="jogador")

    
                                             