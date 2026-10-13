from sqlalchemy import ForeignKey, create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional
import os
from dotenv import load_dotenv

class Base(DeclarativeBase):
    pass

class Time(Base):
    __tablename__ = "tabela_time"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    numero_camisa: Mapped[int] = mapped_column(Integer)
    posicao: Mapped[str] = mapped_column(String(250))

    jogadores: Mapped[List["Jogador"]] = relationship(back_populates="time")

class Jogador(Base):
    __tablename__ = "tabela_jogador"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    numero_camisa: Mapped[int] = mapped_column(Integer)
    posicao: Mapped[str] = mapped_column(String(250))
        
    time_id: Mapped[int] = mapped_column(ForeignKey("tabela_time.id"))
    time: Mapped["Time"] = relationship(back_populates="jogadores")

load_dotenv()

# buscando as variáveis de ambiente
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# definição do banco de dados
engine = create_engine(
f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

Base.metadata.create_all(engine)

# configuração para criar o arquivo de banco de dados
Base.metadata.create_all(engine)

# abrir a sessão
with Session(engine) as session:
        # criar uma pessoa
    t = Time (nome="202-info",
                numero_camisa="10",
                posicao="ala_esquerda" 
            )

# criar um celular
    j1 = Jogador (id = 2131241941, nome = "Ariel",
        numero_camisa = "10",  posicao = "ala_esquerda")

# informar o DONO do celular
    t.jogadores.append(j1)

# adicionar os objetos na sessão
    session.add(t)
    session.add(j1)
    
# confirmar a inserção no banco de dados
    with Session(engine) as session:
        t = Time(
        nome="202-info",
        numero_camisa=10,
        posicao="ala_esquerda"
    )

    j1 = Jogador(
        id=2131241941,
        nome="Ariel",
        numero_camisa=10,
        posicao="ala_esquerda"
    )

    # Associar o jogador ao time
    t.jogadores.append(j1)

    # Salvar o time e o jogador
    session.add(t)
    session.commit()

    print("Banco de dados criado (se não existia), tabela criada (se não havia) e dados inseridos no banco")
