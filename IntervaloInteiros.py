# numero1 = int(input("Digite um numero: "))
# numero2 = int(input("Digite outro numero: "))

# if numero1>numero2:
#     while (numero1+1) < numero2 :
#         numero1 += 1
#     print(f"{numero1}")
# else :
#     while(numero2-1) > numero1:
#         numero2 -= 1
#         print(f"{numero2}")

num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))
    
if num1 <= num2:
    passo = 1
else:
    passo = -1
    
print(f"Números no intervalo entre {num1} e {num2}:")

for i in range(num1,num2 + passo, passo):
    print(i, end=" ")