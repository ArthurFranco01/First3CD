vendas_brutas = [(101, "Monitor", 5, 1200.0), (102, "Mouse", 50, 80.0), (103,
"Teclado", 8, 150.0), (104, "Case", 3, 50.0)]
tupla = ("ID_Produto", "Nome", "Quantidade", "Preço_Unitário")
valor = 0
ValoresQntd = []
PrecoProduto = []
for _ in tupla:
    if _ == "Quantidade":
        for i in vendas_brutas:
            ValoresQntd.append(vendas_brutas[valor][2])
            print(ValoresQntd)
            valor += 1
        valor = 0
        for z in ValoresQntd:
            if z <10:
                print(f"estoque baixo do produto: {vendas_brutas[ValoresQntd.index(z)][1]}")
        somaPreco = 0
        
ponto = 0
Valor = 0
ReajustePreco = 0
ValorReajuste = 0
for _ in vendas_brutas:
    Valor += vendas_brutas[ponto][2]* vendas_brutas[ponto][3]
    ReajustePreco = vendas_brutas[ponto][3] * 0.90
    ValorReajuste += vendas_brutas[ponto][2]* ReajustePreco
    print(f'O preço do produto {vendas_brutas[ponto][1]} após o reajuste de preço é: {ReajustePreco}')
    ponto+=1
print(f'o valor do inventário é: R${Valor}')
print(f'o valor do inventário após o reajuste de valor é: R${ValorReajuste}')

       
    