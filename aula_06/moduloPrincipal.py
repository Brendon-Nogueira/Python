from script import *

myList =[]
print("Preenchendo lista...")
preencheInventario(myList)
print("Lista preenchida com sucesso!")
listaInventario(myList)

print("Localizando nome...")
localizaNome(myList)
print("Nome localizado com sucesso!")
depreciar(myList, 20)

print("Excluindo serial...")
print (excluirSerial(myList))
listaInventario(myList)

print("Resumindo valores...")
resumeValores(myList)



