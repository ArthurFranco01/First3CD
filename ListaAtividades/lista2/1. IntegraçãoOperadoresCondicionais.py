peso = float(input("Digite seu peso(KG): "))
altura = float(input("Digite sua altura(M): "))
IMC = peso/ (altura * altura)
print(f"Seu IMC é : {IMC:.2f}")

if IMC <= 18.5:
    print("Abaixo do peso")
elif 18.5 <= IMC <= 24.9:
    print("Peso normal")
elif 25 <= IMC <=29.9 :
    print("Sobrepeso")
else:
    print("Obesidade")