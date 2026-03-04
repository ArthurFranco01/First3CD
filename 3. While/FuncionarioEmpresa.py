ano = 1995
Salario = 1000
Aumento = 1.5 / 100
while ano != 2024:
    ano += 1
    if ano == 1996:
        Salario = Salario + (Salario * Aumento)
    else:
        Aumento *= 2
        Salario = Salario + (Salario * Aumento)
    print(f"Salario atual: {Salario}")