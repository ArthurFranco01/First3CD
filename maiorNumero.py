x = range(5)
maiorNumero= float('-inf')

for i in x:
    numero = float(input(f"Digite o {i + 1} número: "))
    if numero > maiorNumero:
        maiorNumero = numero
print(f"O maior de todos é esse", maiorNumero)