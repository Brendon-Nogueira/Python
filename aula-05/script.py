#iventario
inventario=[]
print("Inventário, deseja cadastrar os componentes / equipamentos:")
resposta=input("Digite S para sim ou N para não: ")
while resposta=="S":
    inventario.append(input("Digite o nome do componente / equipamento: "))
    inventario.append(float(input("Digite o valor do componente / equipamento: ")))
    inventario.append(int(input("Digite o número serial:")))
    inventario.append(str(input("Digite o Departamento responsável pelo equipamento:")))
    resposta= input("Digite \"S\" para continuar ou \"N\" para sair: ").upper()

    for elemento in inventario:
       print(elemento)
