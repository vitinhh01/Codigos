from a1_modelo_simples import Pessoa, pessoas_interno

# esta função retorna a lista de pessoas
# em um formato a ser exibido pela tabela do streamlit
# está armazenada na lista interna
def retornar_pessoas_formato_tabela():   

    # converte a lista de objetos para um formato
    # que o streamlit consegue mostrar
    dados_no_formato = {
        "Nome": [p.nome for p in pessoas_interno],
        "Email": [p.email for p in pessoas_interno],
        "Telefone": [p.telefone for p in pessoas_interno]
    }

    # retorna os dados
    return dados_no_formato

# esta função insere uma pessoa
def inserir_pessoa(nome : str, email : str, telefone : str):
    
    # cria uma pessoa
    nova = Pessoa(nome, email, telefone)
    
    # adiciona no cadastro interno
    pessoas_interno.append(nova)    