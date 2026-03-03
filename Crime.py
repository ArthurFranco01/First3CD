
pergunta1 = input("Telefonou para a Vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da Vítima? ")
pergunta4 = input("Devia para a Vítima? ")
pergunta5 = input("Já trabalhou com a Vítima? ")

respostas_positivas = 0
if pergunta1 == 'sim': respostas_positivas += 1
if pergunta2 == 'sim': respostas_positivas += 1
if pergunta3 == 'sim': respostas_positivas += 1
if pergunta4 == 'sim': respostas_positivas += 1
if pergunta5 == 'sim': respostas_positivas += 1


if respostas_positivas == 2:
    print("Suspeito")
elif respostas_positivas == 3 or respostas_positivas == 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")

print(f"Número de respostas positivas: {respostas_positivas}")