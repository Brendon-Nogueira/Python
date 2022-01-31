#import da função
from managerUsers import ask, inserir
#dicionario de usuarios 
usuarios ={}

#instruções de acesso
opcao = ask()

#loop de acesso
while opcao != "S":
    if opcao == "I":
      opcao = ask()
      inserir(usuarios)
         

        
        
        
    
    
