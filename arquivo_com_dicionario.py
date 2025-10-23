#Dicionário a ser escrito
books = {'cadastro':1,'nome':'As Estrelas','autor':'Tabata','disponivel':1}

livro = str(books) + '\n'


arquivo = open("livros.txt", "at")
arquivo.write(livro)


