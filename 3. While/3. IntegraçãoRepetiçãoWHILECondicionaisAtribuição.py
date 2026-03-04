saldo = 500
print("---------BANCO FRANCO'S----------------")
print(f"SALDO: {saldo}")
escolha = 0
while escolha != 3 :
    escolha =int(input("para Depositar: digite (1) \npara Sacar: digite (2) \npara Sair: digite (3)\n"))
    if escolha == 1:
        valorDeposito = float(input("Digite o valor do depósito: "))
        saldo += valorDeposito
        print(f"Depósito realizado! Saldo atual: {saldo} \n")
    elif escolha == 2:
        valorSaque = float(input("Digite o valor do saque: "))
        if valorSaque > saldo:
                print("Saldo insuficiente")
                print(f"Saldo Disponível: {saldo}\n")
        else:
                saldo -= valorSaque
                print(f"Saque Realizado! Saldo atual: {saldo} \n")
print("SESSÃO ENCERRADA! OBRIGADO POR UTILIZAR BANCO FRANCO'S")
    