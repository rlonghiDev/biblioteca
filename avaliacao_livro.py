import json

def avaliacao_livro(regitro_do_livro):

    registro_livro = int(regitro_do_livro)

    avaliacao = input("Digite sua avaliação para o livro de 0 a 5 ou 'n' para não avaliar\n")
    
    if avaliacao == 'n':
        return
    
    avaliacao = int(avaliacao)
    
    novas_linhas = ''       
    
    
    with open("livros.txt", "r") as arq:
        
        for linha in arq:
            dicionario = eval(linha)
            
            
            print("Campo dicionario: ",dicionario["Registro"],type(dicionario["Registro"]))
            print("Registro do Livro: ",registro_livro,type(registro_livro))
            print(dicionario["Registro"] == registro_livro)
            
            
            if dicionario["Registro"] == registro_livro:
                dicionario["rating"] = avaliacao
                print("Avaliacao: ",avaliacao,"escrita")                
           
            novas_linhas += json.dumps(dicionario) + '\n'
        
        
        arq.close()
        
    with open("livros.txt", "wt") as arq:
        
        arq.write(novas_linhas)
        
    arq.close()
        
        
        
            
    
 
 
 
    
#avaliacao_livro(5)



    
    
    
            
        
        

