import datetime
import cadastra_livro
import ultimo_registro
import json


def cadastrar_leitor():
    nome = input("Digite o nome do Leitor\n")
    escola = input("Informe qual escola está matriculado\n")
    turma = input("Informe o curso que o leitor está inscrito\n")
    ano_cadastro = datetime.date.today().year

    #Produra o último registro de livro para partir determinar próximo registro.
    registro_leitor = ultimo_registro.procura_ultimo_registro("leitor")

    leitor = {}
    leitor["nome"]=nome
    leitor["escola"]=escola
    leitor["turma"] = turma
    leitor["ano"]=ano_cadastro
    leitor["Registro"] = registro_leitor

    leitor_str = json.dumps(leitor) + "\n"

    with open("leitores.txt","at") as arq:
        arq.write(leitor_str)

    arq.close()
