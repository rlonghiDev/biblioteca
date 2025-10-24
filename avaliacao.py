## Recebe a avaliação e escreve no arquivo
def avaliacao(tipo,Registro,nota):

    ##Prepara os dados e escreve no arquivo 

    lista_para_escrever = str(tipo) + ',' + str(Registro) + ',' + str(nota) + '\n'

    with open("avaliacao.txt","at") as ava:

      ava.write(lista_para_escrever)
    
    ava.close()




def informa_media_avaliacao(tipo,Registro):
    # tipo => 0 se for sobre atendimento 
    # tipo => 1 se for sobre livro

    ## Registro => 0 se for sobre atendimento 
    ## Registro diferente de 0 para entregar a avaliação correspondente ao livro, Registro indica qual é o livro 
    

    soma_notas_atendimento = 0
    soma_notas_livro = 0
    media_atendimento = 0
    media_livro = 0
    c1 = 0
    c2 = 0

    with open("avaliacao.txt", "r") as ava:
          
        lista_int = []
        

        for linha in ava:
            linha = linha.replace('\n','')
            lista = linha.split(',')
            print(lista)
            # Altera 
            for i in lista:
                lista_int.append(int(i))
                                

            print(lista_int,'\n')

            #identifica avaliação de atendimento
            if lista_int[0] == 0:
                soma_notas_atendimento += lista_int[2]
                c1 += 1

            #Identifica avaliação de livro

            if lista_int[0] == 1:
                if lista_int[1] == Registro:
                    soma_notas_livro += lista_int[2]
                    c2 += 1

            lista_int.clear()
    ava.close()

    if tipo == 0:
        if soma_notas_atendimento > 0:
            media_atendimento = (soma_notas_atendimento / c1)
            #print(media_atendimento)
            return media_atendimento

    if tipo == 1:
        if soma_notas_livro > 0:
            media_livro = (soma_notas_livro/c2)
            #print(round(media_livro,1))
            return media_livro



