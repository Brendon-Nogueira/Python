def preencheInventario(lista):
    resposta = "S"
    while resposta == "S":
     equipamento = [
        input("Nome do equipamento: "),
        float(input("Preço do equipamento: ")),
        int(input("Número serial: ")),
        input("Departamento responsável: ")]
     lista.append(equipamento)
     reposta = input("Digite \"S\" para continuar: ")
     
def listaInventario(lista):
    for index in lista:
        print("Nome do equipamento: ", index[0])
        print("Preço do equipamento: ", index[1])
        print("Número serial: ", index[2])
        print("Departamento responsável: ", index[3])


def localizaNome(lista):
    source = input("Digite o nome do equipamento: ")
    for element in lista:
        if source == element[0]:
            print("Valor do equipamento: ", element[1])
            print("Número serial: ", element[2])


def depreciar(lista , porcentagem):
    depreciacao=input("Digite o nome do equipamento: ")
    for element in lista:
        if depreciacao == element[0]:
            print("Valor antigo: ", element[1])
            element[1]=element[1] * (1-porcentagem/100)
            print("Valor depreciado: ", element[1])
            

def excluirSerial(lista):
    serial = int(input("Digite o número serial do equipamento: "))
    for element in lista:
        if serial == element[2]:
            lista.remove(element)
            return ("Equipamento excluído com sucesso!")

def resumeValores(lista):
   valores =[]
   for index in lista:
         valores.append(index[1])
         if len(valores)>0:
             print("Valor total: ", sum(valores))
             print("Equipamento mais caro: ", max(valores))
             print("Equipamento mais barato: ", min(valores))
        
            
            
            
            
            
            
            
            
            
            
                    
