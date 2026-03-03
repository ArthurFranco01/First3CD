saldo = 1000
saldo_inicial = saldo
caracProibidos = "*#"
auditor = ""
while auditor != 1 :
    auditor = str(input("Digite o nome do auditor:"))
    if "*" in auditor:
        print("Caracteres proibidos! digite novamente")
    elif "#" in auditor:
        print("Caracteres proibidos! digite novamente")
    else:
        print("auditor correto!")
        print(saldo_inicial)
        break

for _ in range(1, 5) :
    transações = int(input("Faça uma transação:"))
    if transações < (saldo *-1):
        print("Erro na operação! Débito maior que o saldo")
    else:
        saldo += transações
        if transações > 500:
            print("Transação de alto valor")
            print(f"saldo atual: {saldo}")
        elif transações <= 0:
            print(f"saldo atual: {saldo}")
    
        else: 
         print(f"saldo atual: {saldo}")