def ask ():
    return  input("Seja bem vindo ao sistema, escolha uma opção.\n" +
              "<I> para inserir um novo usuário\n" +
              "<P> para pesquisar um usuário\n" +
              "<E> para excluir um usuário\n" +
              "<L> para listar um usuário:\n" +
              "<S> para sair\n").upper()
    
    def inserir (dicionario):
       dicionario = usuarios[input("Digite o login do usuário: ").upper(),
                 input("Digite o nome do usuário: ").upper(),
                 input("Digite a última data de acesso: "),
                  input("Digite o setor de acesso do usuário: ").upper()]
       
       return  dicionario
                
        
