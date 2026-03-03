senha = ""
while senha != "python123" :
    senha = str(input("Digite a senha correta: "))
    if senha != "python123":
        print("Acesso negado! senha incorreta")
    else:
        print("Acesso permitido!") 