nome = input("Olá! Qual é o seu nome? ")
renda = float(input("Qual é a sua renda mensal? R$"))
gasto_mensal = float(input("Qual é o seu gasto mensal? R$"))
coragem = int(input("De 1 a 10, qual é o seu nível de coragem para investimentos? "))

if gasto_mensal > renda:
    print(f"\n{nome}, alerta de Emergência Financeira! Seus gastos são maiores que sua renda.")
else:
    sobra = renda - gasto_mensal
    reserva_seguranca = 6 * gasto_mensal
    if sobra < reserva_seguranca:
        print(f"\n{nome}, você precisa economizar mais R${reserva_seguranca - sobra:.2f} para ter uma reserva de segurança.")
    else:
        print(f"\n{nome}, você já tem uma reserva de segurança.")

    if coragem < 4:
        investimento = "Tesouro Direto"
    elif 4 <= coragem <= 7:
        investimento = "Fundos Imobiliários"
    else:
        investimento = "Ações de Tecnologia"
    print(f"Com base no seu perfil, recomendamos investir em {investimento}.")

    anos_investir = int(input("Quantos anos você pretende investir? "))
    print(f"\n{nome}, com disciplina e {anos_investir} anos de investimento, você pode alcançar grandes objetivos!")