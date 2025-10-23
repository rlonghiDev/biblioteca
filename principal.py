import time
import datetime
import cadastra_livro #Biblioteca criada para incluir novos livros
import cadastro_leitor
import relatorios
import ultimo_registro
import emprestimos
import confirma
import datetime



while True:
    
    ### Apresentação e Menu inicial ##
    print("""
          Bem vindo ao sistema gerenciador de Biblioteca !
          
          Escolha a opção desejada:
          1 - Opções sobre livro
          2 - Opções sobre leitor
          3 - Menu empréstimo 
          4 - Imprimir um relatório
          5 - Sair 

          """)
    
    #Recebe a escolha e verifica opção válida
    menu_principal = input("Digite a opção desejada\n")
    if menu_principal != '1' and menu_principal != '2' and menu_principal != '3' and menu_principal != '4' and menu_principal != '5':
        print("Opção incorreta, tente novamente")
        time.sleep(3)
        continue
    
    ######Saída do Looping #####
    if menu_principal =='5':
        break
    
    ####Início Cadastra Livro ###
       
    if menu_principal == '1':
        cadastra_livro.menu_livro()
        
   
    #### Início Cadastra Leitor ###

    
    if menu_principal == '2':
        cadastro_leitor.cadastrar_leitor()
        ficha_leitor = confirma.confirma_cadastro("leitor")
        confirmacao_leitor = relatorios.monta_string_leitor(ficha_leitor)
        print(confirmacao_leitor)

    ### Final Cadastra Leitor ###


    ##### Menu empréstimo ####

    
    if menu_principal == '3':

        while True:

            print("""

                Digite 1 para informar o empréstimo
                Digite 2 para informar devolução
                Digite 3 para voltar
                  
                """)
            
            opcao = input("Informe o que deseja fazer\n")

            if opcao == '3':
                break
            
          
               

            if opcao == '1': # Informar Empréstimo 
                registro_leitor = input("Digite o número de registro do Leitor\n")
                registro_livro = input("Digite o número de Registro do Livro\n")
                cartao_emprestimo = emprestimos.realiza_emprestimo(registro_leitor,registro_livro)
                
                
            if opcao == '2':
                emprestimos.apaga_emprestimo()
                
                #cartão_emprestimo


            
    ##### Relatórios ####                

    if menu_principal == '4':

        while True:

            print("""
                Digite 1 para relatório de livros
                Digite 2 para relatório de leitores
                Digite 3 para relatório de empréstimos
                Digite 4 para voltar ao menu principal

                """)

            outra_escolha = input("Informe a opção desejada: \n")
        

            if outra_escolha == '4':
                break

            if outra_escolha == '1':
                relatorios.relatorio_livros()

            if outra_escolha == '2':
                relatorios.relatorio_leitores()
                
            if outra_escolha == '3':
                relatorios.relatorio_emprestimo()

        ##### Final Relatório Leitores ######
