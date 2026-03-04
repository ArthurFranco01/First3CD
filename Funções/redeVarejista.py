def limpar_vendas(valores):
    nova_lista = []
    for x in valores:
        if x < 10000 and x > 0:
            nova_lista.append(x)
    return nova_lista

def analisar_dados(z):
    soma = sum(nova_lista)
    media =sum(nova_lista) / len(nova_lista)
    return  soma, media

def definir_status(z):
    x = ""
    if z < 2000:
        x = "Performance Crítica"
    elif z > 2000 and z < 5000:
        x = "Performance Estável"
    else :
        x = "Alta Performance"
    return x
Vendas_validas = 1
Filial = str(input("Digite o nome da filial: ")) 
valores = []
valor = ""
while valor != 0:
    valor = (float(input("Informe o valor da venda: ")))
    if valor == 0:
        break
    else:
        valores.append(valor)
print("Criando lista de vendas.......")
print(valores)
print("limpando valores de vendas maiores de dez mil.......")
nova_lista = limpar_vendas(valores)
print(nova_lista)
soma, media = analisar_dados(nova_lista)
print(f"A soma da lista limpa: {soma}")
print(f"A media da lista limpa: {media:.2f}")
print("Calculando a performance das vendas......")
performance = definir_status(media)
print(f"a perfomance das vendas é de {performance}")
print("----RELATÓRIO DE VENDAS----")
print(f"Nome da filial:{Filial}")
print(f"Status da performance: {performance}")
print(f"faturamento:{soma} \nmédia:{media:.2f}")
print("Lista de vendas válidas:")
for x in valores:
        if x < 10000 and x > 0:
            print(f"{Vendas_validas}. {x}\n")
            Vendas_validas +=1
        else:
            continue