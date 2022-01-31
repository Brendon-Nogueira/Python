#Listas múltiplas 
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Digite o equipamento: "))
    valores.append(float(input("Digite o valor: ")))
    seriais.append(int(input("Digite o serial: ")))
    departamentos.append(input("Digite o departamento: "))
    resposta = input("Deseja continuar: \"S\" ").upper()
    
source = input ("\nDigite o nome do equipamento, que está buscando: ")
for index in range(0,len(equipamentos)):
    if source==equipamentos[index]:
        print("Valor: ", valores[index])
        print("Serial: ", seriais[index])
        print("Departamento: ", departamentos[index])
