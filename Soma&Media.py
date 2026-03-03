# num1 = float(input("Digite o primeiro numero:"))
# num2 = float(input("Digite o segundo numero:"))
# num3 = float(input("Digite o terceiro numero:"))
# num4 = float(input("Digite o quarto numero:"))
# num5 = float(input("Digite o quinto numero:"))

# soma = num1 + num2 + num3 + num4 + num5
# print(f"a soma é {soma}")
# media = (num1 + num2 + num3 + num4 + num5) /5
# print(f"a media é {media}")

x = range(5)
TotalNum= 0
for i in x:
    numero = float(input(f"Digite o {i + 1} número: "))
    TotalNum += numero
    
    
MediaNum = TotalNum /5
print(f"A soma desses numeros é {TotalNum}")
print(f"A media desses numeros é {MediaNum}")