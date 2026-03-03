vogal = "aeiouAEIOU"
x = str(input("Digite seu nome completo: "))
qntdVogal = 0
for i in x:
    if i in vogal:
        qntdVogal +=1
        print(i)
print(f"A quantidade de vogais em {x} é: {qntdVogal}")
