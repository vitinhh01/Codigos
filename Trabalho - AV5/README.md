# Trabalho AV5 — Desenvolvimento do Projeto

## Etapas do Desenvolvimento

### 1. Desenvolvimento do programa
Utilizamos um programa já existente como base para desenvolver nosso projeto. Aproveitamos duas classes e seus atributos, realizando as alterações necessárias para adaptar o código às nossas necessidades.

### 2. Configuração do ambiente
Utilizamos o terminal do VS Code e o auxílio de prompts para instalar as bibliotecas necessárias ao funcionamento do programa, como `SQLAlchemy`, `PyMySQL` e outras dependências.

### 3. Configuração do banco de dados
Criamos o arquivo `.env` para armazenar as informações de conexão com o banco de dados. Em seguida, utilizamos o XAMPP e o MySQL para configurar o banco e conectá-lo ao projeto por meio do driver `PyMySQL`.

### 4. Execução do programa
Após conectar o projeto ao banco de dados, utilizamos o comando `uv run` para executar o código e verificar se as informações estavam sendo enviadas e salvas corretamente.

### 5. Correção de erros
Durante o desenvolvimento, identificamos e corrigimos pequenos problemas no código, principalmente relacionados à escrita e à concordância. Também adicionamos as opções de conexão com SQLite e MySQL.

### 6. Organização do banco de dados
Dependendo do banco de dados escolhido, o programa utiliza uma pasta específica para armazenar os dados. No caso do SQLite, o banco é armazenado localmente em um arquivo; no MySQL, os dados ficam no servidor configurado.

### 7. Integração das informações
Transferimos as informações necessárias do banco de dados para o VS Code, organizando os dados e ajustando o programa conforme os requisitos solicitados pelo professor.

### 8. Envio para o repositório
Por fim, executamos o comando `git commit` para registrar as alterações realizadas no projeto e prepará-las para o envio ao repositório.

## Tecnologias e ferramentas utilizadas

- **Python:** desenvolvimento do programa.
- **VS Code:** edição e execução do código.
- **SQLAlchemy:** integração e manipulação do banco de dados.
- **PyMySQL:** conexão entre Python e MySQL.
- **SQLite:** armazenamento local dos dados.
- **MySQL:** gerenciamento do banco de dados.
- **XAMPP:** ambiente utilizado para executar o servidor MySQL.
- **Git:** controle de versão do projeto.
- **UV:** gerenciamento do ambiente e execução do projeto.
- **Arquivo `.env`:** armazenamento das configurações de conexão.