nome = input ("Digite seu nome: ")
idade = int(input ("Digite sua idade: "))
print ("Olá", nome, "sua idade é", idade)

if idade >= 18:
    print ("Você é maior de idade:" , nome)
else: 
    print ("Você é menor de idade, então precisa de um responsável", nome)