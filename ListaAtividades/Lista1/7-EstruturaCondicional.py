idade = int(input("Digite sua idade: "))

if idade >= 5 and  idade  <= 12 :
    print(f"Nadador Classificação Infantil. Idade {idade}")
elif idade >= 13 and idade <= 17:
    print(f"Nadador Classificação Juvenil. Idade {idade}")
elif idade >= 18 :
    print(f"Nadador Classificação Adulto. Idade {idade}")
else:
    print("Inválido! Idade inferior a 5.")