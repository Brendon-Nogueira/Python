inventario =[]
resposta = "S"

#adicionar item no inventario
while resposta == "S":
    produtos=[input("Digite o nome do produto: "),
                 float(input("Valor: ")),
                 int(input("Codígo do produto: ")),
                 input("Digite o setor responsável por está validação: ")]
    inventario.append(produtos)
    resposta = input("Digite \"S\"para continuar: ") .upper()
    print(inventario)
    
    #exibe os produtos cadastrados no inventario
    for i in inventario:
        print("Produto: ", i[0])
        print("Valor: ", i[1])
        print("Codigo: ", i[2])
        print("Setor: ", i[3])
        
    source = input ("Digite o nome do produto que desejá localizar: ")
    for y in inventario:
        if source ==y[0]:
            print("Produto: ", y[0])
            print("Valor: ", y[1])
            print("Codigo: ", y[2])
            print("Setor: ", y[3])
            
            depreciation = input("Digite o valor de depreciação: ")
            for element in inventario:
                if element[0] == source:
                    print("Valor antigo: ", element[1])
                    element[1] = element[1] * 0.10
                    print("Valor atualizado: ", element[1])
                    
            cod = input("Digite o código do produto que deverá ser removido: ")
            for index in inventario:
                if index[2] == cod:
                    inventario.remove(index)
                    print("Produto removido com sucesso!")
                    break
            else:
                print("Produto não encontrado!")
            
            for index in inventario:
                print("Produto: ", index[0])
                print("Valor: ", index[1])
                print("Codigo: ", index[2])
                print("Setor: ", index[3])
            
        valores = []
        for element in inventario:
            valores.append(element[1])
            if len (valores)>0:
                print("Valor total: ", sum(valores))
                print("Valor maximo: ", max(valores))
                print("Valor minimo: ", min(valores))