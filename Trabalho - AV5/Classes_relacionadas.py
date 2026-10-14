from sqlalchemy import (ForeignKey, create_engine, String, Integer)
from sqlalchemy.engine import URL
from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column, Session, relationship)
from typing import List
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

    jogadores: Mapped[List["Jogador"]] = relationship(
        back_populates="time"
    )


class Jogador(Base):
    __tablename__ = "tabela_jogador"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    numero_camisa: Mapped[int] = mapped_column(Integer)
    posicao: Mapped[str] = mapped_column(String(250))

    time_id: Mapped[int] = mapped_column(
        ForeignKey("tabela_time.id")
    )
    time: Mapped["Time"] = relationship(
        back_populates="jogadores"
    )


load_dotenv()


def escolher_banco():
    print("\n===== ESCOLHA O BANCO DE DADOS =====")
    print("1 - SQLite")
    print("2 - MySQL")

    opcao = input("Digite sua opção: ").strip()

    if opcao == "1":
        engine = create_engine("sqlite:///banco.db")
        print("Você escolheu SQLite!")

    elif opcao == "2":
        mysql_user = os.getenv("MYSQL_USER")
        mysql_password = os.getenv("MYSQL_PASSWORD", "")
        mysql_host = os.getenv("MYSQL_HOST")
        mysql_port = os.getenv("MYSQL_PORT", "3306")
        mysql_database = os.getenv("MYSQL_DATABASE")

        if not all([mysql_user, mysql_host, mysql_database]):
            raise ValueError(
                "Verifique as configurações do MySQL no arquivo .env"
            )

        url = URL.create(
            "mysql+pymysql",
            username=mysql_user,
            password=mysql_password,
            host=mysql_host,
            port=int(mysql_port),
            database=mysql_database,
        )

        engine = create_engine(url)
        print("Você escolheu MySQL!")

    else:
        print("Opção inválida! Tente novamente.")
        return escolher_banco()

    return engine


def main():
    # Escolher o banco de dados
    engine = escolher_banco()

    # Criar as tabelas no banco escolhido
    Base.metadata.create_all(engine)

    # Inserir os dados
    with Session(engine) as session:
        t = Time(
            nome="202-info",
            numero_camisa=10,
            posicao="ala_esquerda"
        )

        j1 = Jogador(
            nome="Ariel",
            numero_camisa=10,
            posicao="ala_esquerda"
        )

        # Associar o jogador ao time
        t.jogadores.append(j1)

        # Salvar time e jogador
        session.add(t)
        session.commit()

        print("\nBanco conectado!")
        print("Tabelas criadas, se necessário.")
        print("Time e jogador inseridos com sucesso!")


if __name__ == "__main__":
    main()