def Fpasso1() :
        passo1 = int(input("escolha caminho de pedras(digite 1) ou caminha de árvores(digite 2)"))
        if passo1 == 1:
            print("OH NÃO! o caminho de pedras levou você a uma grande montanha, agora terá que supera-la!")
            Fpasso3()
        elif passo1 == 2:
            print("Que ótimo! esse caminho levou até um lindo campo com árvores gigantes! ")
            print("Vamos continuar a exploração")
            Fpasso7()
        else:
            print("Escolha o caminho entre 1 ou 2")

def Fpasso2() :
        passo2 = int(input("escolha o caminho 1 (digite 1) escolha o caminho da direita (digite 2)"))
        if passo2 == 1 :
            print("Esse caminho te levou até a beira de um abismo! retornando ao início...")
            Fpasso1()
        if passo2 == 2:
            
            Fpasso7()
        else:
            print("Escolha o caminho entre 1 ou 2")

def Fpasso3():
    passo3 = int(input("Você opta por escalar a montanha (digite 1) ou seguir o caminho ao redor da montanha (digite 2)"))
    if passo3 == 1 :
        Fpasso4()
    elif passo3 == 2:
        Fpasso5()
    else: 
        print("Escolha o caminho entre 1 ou 2")
def Fpasso4():
    escalar = int(input("digite um numero entre 1 e 10 para tentar escalar a montanha"))
    if escalar == 1 or escalar == 8 or escalar == 9 or escalar == 4 :
        print("Parabéns! você conseguiu escalar a montanha e continuar a exploração!")
        Fpasso7()
    elif escalar < 0 or escalar > 10:
        print("Escolha um número entre 1 e 10.")
        Fpasso4()
    else:
        print("Infelizmente, a escalada foi muito difícil e você teve que desistir. Retornando ao início...")
        Fpasso1()     
def Fpasso5():
    print("Você contornou a montanha com sucesso! continuando exploração...")
    Fpasso7()
def Fpasso7():
        global dados
        print("Meu Deus! você encontrou uma área rica em minerais, onde pode coletar dados valiosos para a tribulação ")
        coletarDados = int(input("você quer coletar dados? sim(digite 1) não(digite 2)"))
        if coletarDados == 1 :
            print("Você coletou dados valiosos!")
            dados += 1
            Fpasso8()

        elif coletarDados == 2:
            print("Você decidiu não coletar dados.")
            dados = 0
            Fpasso8()
            

def Fpasso8():
     Decisao = int(input("Você deseja continuar explorando o planeta? sim(digite 1) não(digite 2)"))
     if Decisao == 1:
        print("Você decidiu continuar explorando o planeta!")
        Fpasso1()
     elif Decisao == 2:
        print("Você decidiu encerrar a exploração do planeta. Voltando para a nave...")
        Fpasso9()
     else:
        print("Escolha entre 1 ou 2.")

def Fpasso9():
     print("Fim da exploração! Você coletou dados valiosos e contribuiu para a missão da tribulação. Voltando para o planeta Terra...")
     print("resumo da exploração: ")
     print(f"Você coletou {dados} dados valiosos.")


print("Bem vindo ao planeta Alphara-7, pronto para explorar e conhecer esse planeta misterioso?!")
print("Assim que a exploração começa, você se depara com dois caminhos")
dados = 0
Fpasso1()
            
   
