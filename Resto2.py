Contagem = 0
for numero in range(1000, 2001):
    if numero % 11 == 2:
        Contagem += 1
        print(f"{numero}")
print(f"{Contagem} numeros")       