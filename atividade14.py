porhora = int(input("Quanto voce ganha por hora?"))
hora = int(input("Quantas horas trabalhada?"))

total = (porhora*hora)
print ("Seu salario bruto é:" ,total)

ir = total * 0.11
inss = total * 0.08
sindicato = total * 0.05

liquido = total-ir-inss-sindicato

print("Salario bruto: R$",total)
print("IR: R$",ir)
print("INSS: R$" ,inss)
print("Sindicato: R$",sindicato)
print("Seu salario liquido é,",liquido)

