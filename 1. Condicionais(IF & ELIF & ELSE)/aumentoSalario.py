Salario = int(input("Informe seu salário: "))
percentualAumento = ""
ValorAumento = 0
NovoSalario = 0

if Salario > 1500:
    percentualAumento = 0.05
    NovoSalario = Salario + (Salario * percentualAumento)
elif Salario > 700 and Salario <= 1500:
    percentualAumento = 0.10
    NovoSalario = Salario + (Salario * percentualAumento)
elif Salario > 280 and Salario <= 700:
    percentualAumento = 0.15
    NovoSalario = Salario + (Salario * percentualAumento)
else:
    percentualAumento = 0.20
    NovoSalario = Salario + (Salario * percentualAumento)
    
valorAumento = NovoSalario - Salario
print(f"Salario antes: {Salario}")
print(f"Percentual aumento aplicado: {percentualAumento}")
print(f"Novo salario: {NovoSalario}")
print(F"valor do aumento: {valorAumento:.2f}")