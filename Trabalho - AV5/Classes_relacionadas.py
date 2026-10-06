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
    posicao: Mapped[str] = mapped_column(String(250))

class Jogador(Base):
    __tablename__ = "tabela_jogador"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    numero_camisa: Mapped[int] = mapped_column(Integer)
    posicao: Mapped[str] = mapped_column(String(250))
        
    time_id: Mapped[int] = mapped_column(ForeignKey("tabela_time.id"))
    Time: Mapped["time"] = relationship(back_populates="jogador")

# chave estrangeira :-)
    pessoa_id: Mapped[int] = mapped_column(ForeignKey("tabela_time.id"))
    # atributo para acesso ao objeto inteiro :-)
    # esse atributo está "ligado" ao atributo "celulares", pois
    # é usado para "popular" a lista de celulares da classe Pessoa
    pessoa: Mapped["time"] = relationship(back_populates="jogadores")    


    
engine = create_engine("sqlite:///time_e_jogadores.db")

# configuração para criar o arquivo de banco de dados
Base.metadata.create_all(engine)

# abrir a sessão
with Session(engine) as session:
        # criar uma pessoa
    t = time (nome="202-info",
                numero_camisa="10",
                posicao="ala_esquerda" 
            )

# criar um celular
    j1 = Jogador( id = 2131241941, nome = "Ariel",
        numero_camisa = "10"  posicao = "ala_esquerda")

# informar o DONO do celular
    j1.time = t

# adicionar os objetos na sessão
    session.add(t)
    session.add(j1)
    
# confirmar a inserção no banco de dados
    session.commit()

    print("Banco de dados criado (se não existia), tabela criada (se não havia) e dados inseridos no banco")
