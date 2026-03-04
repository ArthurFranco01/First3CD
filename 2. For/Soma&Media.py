x = range(5)
TotalNum= 0
for i in x:
    numero = float(input(f"Digite o {i + 1} número: "))
    TotalNum += numero
    
    
MediaNum = TotalNum /5
print(f"A soma desses numeros é {TotalNum}")
print(f"A media desses numeros é {MediaNum}")