import ultimo_registro
import confirma
import relatorios
import json

def cadastrar_livro():

    #Produra o último registro de livro para partir determinar próximo registro.
    num_registro = ultimo_registro.procura_ultimo_registro("livro")

    #Recebe os dados do livro 
    nome = input("Digite o nome do livro\n")
    autor = input("Digite o nome do autor\n")
    qde_disp = int(input("Digite a quantidade disponível do livro\n"))
    qde_uso = 0
    avaliacao_livro = int(input("Digite a sua avaliação do livro de 0 a 5\n"))
    
    ## Coloca as informações no dicionário ##
    livro_dicionario = {}
    livro_dicionario["nome"] = nome
    livro_dicionario["autor"] = autor
    livro_dicionario["Qde_disp"] = qde_disp
    livro_dicionario["Qde_uso"] = qde_uso
    livro_dicionario["rating"] = avaliacao_livro
    livro_dicionario["Registro"] = num_registro

    livro_str = json.dumps(livro_dicionario) + "\n"

    with open ("livros.txt", "at") as arq:
        arq.write(livro_str)
    
    arq.close()
    
    
    
    
def menu_livro():
    while True:
        print("""
              
            Bem vindo ao Menu de opções possíveis com livros:

            1 - Cadastrar um livro 
            2 - Apagar o cadastro de um livro
            3 - Volta as opções anteriores
            
            """)
        
        escolha_do_usuario = input("O que você deseja fazer ?")

        if escolha_do_usuario == "3":
            break

        if escolha_do_usuario == "1":
            cadastrar_livro()
            ficha_livro = confirma.confirma_cadastro("livro")
            confirmacao_livro = relatorios.monta_string_livro(ficha_livro)
            print(confirmacao_livro)


