import datetime

def busca_info(Registro, tipo):
    
    arquivo_para_ler = ''  
    
    if tipo == 'leitor':
        arquivo_para_ler = "leitores.txt"
        
    if tipo == 'livro':
        arquivo_para_ler = "livros.txt"
        
    if tipo == 'emprestimo':
        arquivo_para_ler = "emprestimos.txt"
        
    with open(arquivo_para_ler,"r") as arq:
        
        for linha in arq:
            dicionario = eval(linha)
        
            procura = str(dicionario['Registro'])
            procura = procura.strip()
            Registro = Registro.strip()
            
            if procura == Registro:
                nome = dicionario
                break
                
            else:
                nome = "Nao localizado"
    
    arq.close()#Fecha arquivo            
    
    
    print("O que foi captado:",nome)

Registro = '9'
tipo = 'emprestimo'

busca_info(Registro, tipo)


# Registro = '"Registro": 2'
# indice_para_apagar = ''

# with open("emprestimos.txt","r") as arq: #Abre arquivo no modo leitura
#     lista_de_linhas = arq.readlines()
    
#     arq.close() #Fecha arquivo
    
#     for indice,linha in enumerate(lista_de_linhas):
#         if Registro in linha:
#             indice_para_apagar = indice
        
#     print(type(indice_para_apagar))        
#     ##Remove emprestimo localizado se o registro foi localizado
#     if type(indice_para_apagar) is int:
#         lista_de_linhas.pop(indice_para_apagar)
#         print("Empréstimo encerrado com sucesso")
#     else:
#         print("Empréstimo não foi localizado")
    
# with open("emprestimos.txt","w") as arq: #Abre arquivo modo escrita
        
#     for linha in lista_de_linhas:
#         linha.strip() # Tira eventuais espaços em branco no inicio ou final 
#         #linha = linha + '\n' #Coloca a próxima inserção na linha abaixo
#         arq.write(linha)
    
#     arq.close()
    
        
        
    
    
    
    
    
            







# import json

# def confirma_cadastro(tipo_confirmacao):
    
#     if tipo_confirmacao == 'livro':
#         arquivo_a_ser_lido = 'livros.txt'
    
#     if tipo_confirmacao == 'leitor':
#         arquivo_a_ser_lido = 'leitores.txt'
        
#     if tipo_confirmacao == 'emprestimo':
#         arquivo_a_ser_lido = 'emprestimos.txt'
    
    
    
    
#     with open(arquivo_a_ser_lido,"r") as arq:
#         linha = arq.readlines()

#         arq.close()
    
#     registro = linha[-1].strip()
    
#     return json.loads(registro) 



####### Formatação de Data #####
# from datetime import date
            
# hoje_BD = date.today()
# hoje_BD = str(hoje_BD)
# print(hoje_BD)
# ano = hoje_BD[0:4]
# mes = hoje_BD[5:7]
# dia = hoje_BD[8:10]
# print(f"{dia}/{mes}/{ano}")





## Relatório Livro ##

# def monta_string(dict):
#     linha1 = '#' * 50
#     espacamento = '#' + ' ' * 48 + '#'
#     str21 = 'Título: ' # String [linha2] [posição1]
#     str22 = dict['nome'] # String [linha2] [posição1]
#     linha2 = '#' + str21.rjust(24) + str22.ljust(24) + '#'
#     str31 = 'Autor: '
#     str32 = dict['autor']
#     linha3 = '#' + str31.rjust(24) + str32.ljust(24) + '#'
#     str41 = 'Disponível: '
#     str42 = str(dict['Qde_disp'])
#     linha4 = '#' + str41.rjust(24) + str42.ljust(24) + '#'
#     str51 = 'Registro: '
#     str52 = str(dict['Registro'])
#     linha5 = '#' + str51.rjust(24) + str52.ljust(24) + '#'

#     ficha = (linha1 +'\n'+ espacamento + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + espacamento + '\n' + linha1 + '\n')
#     return ficha


# with open("livros.txt","r") as arq:
    
#     for linha in arq:
#         dicionario = eval(linha)
#         ficha = monta_string(dicionario)
            
#         print(ficha)
            
        



        
# #tabulate

# arq.close()


# string_customizada = "nome:Charlie,idade:35,cidade:Nova York"
# # Divide a string em pares chave:valor e depois em chave e valor
# meu_dicionario = {chave.strip(): valor.strip() for item in string_customizada.split(',') for chave, valor in [item.split(':')]}

# print(meu_dicionario)
# print(type(meu_dicionario))






# import datetime

# nome = input("Digite o nome do Leitor")
# escola = input("Informe qual escola está matriculado")
# turma = input("Informe o curso que o leitor está inscrito")
# ano_cadastro = datetime.date.today().year
# registro_leitor = ''

# leitor ={}
# leitor['nome']=nome
# leitor['escola']=escola
# leitor['turma'] = turma
# leitor['ano']=ano_cadastro
# leitor['Registro'] = registro_leitor

# leitor_str = str(leitor) + '\n'

# with open("leitores.txt","at") as arq:
#      arq.write(leitor_str)

# arq.close()








# with open("livros.txt","r") as arq:
#     linha = arq.readlines()

# arq.close()

# if linha:
#     registro = linha[-1].strip()
# else:
#     registro = 'falhou'
#     print(registro)


# print(type(registro))

# posicao = registro.find('Registro')
# tamanho = len(registro)

# reg = '0'
# trecho_inteiro = registro[posicao:tamanho]
# for i in trecho_inteiro:
#     if i.isdigit():
#         reg += i


# valor = int(reg) + 1


# print("Registro:", valor)

