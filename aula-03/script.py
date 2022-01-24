nome = input ("Digite seu nome: ")
idade = int(input ("Digite sua idade: "))
print ("Olá", nome, "sua idade é", idade)

palentologia = input ("Suspeita de doença infecciosa: ").upper()
 
if idade >= 65:                                                                        
 print ("Necessita de atendimento prioritário:")
elif palentologia =="SIM":
     print ("Necessita de atendimento urgente:")
 
else:
 print ("Necessita de atendimento normal:")
    