primeiros_nomes = ["João", "Lucas", "Lucas", "Gabriel", "Mateus", "Rafael", "Felipe", "Gustavo", "Bruno", "Thiago"]
primeiros_nomes.remove("Lucas")
print(primeiros_nomes)
print(primeiros_nomes.index("João"))
indice = 0
for _ in primeiros_nomes:
    print(_)

    print(indice)
    indice += 1

primeiros_nomes.remove("João")
print(primeiros_nomes)
primeiros_nomes.clear()
print(primeiros_nomes)
