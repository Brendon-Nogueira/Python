equipamentos =[]
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Digite o nome do equipamento: "))
    valores.append(float(input("Digite o valor do equipamento: ")))
    seriais.append(int(input("Digite o serial do equipamento: ")))
    departamentos.append(input("Digite o departamento responsável: "))
    resposta = input("Deseja continuar? \"S\" ").upper()
    
    for index in range(0,len(equipamentos)):
        print("\nEquipamento: ",[index + 1])
        print("Nome...:", equipamentos[index])
        print("Valor..:", valores[index])
        print("Serial..:", seriais[index])
        print("Departamento.:", departamentos[index])
        