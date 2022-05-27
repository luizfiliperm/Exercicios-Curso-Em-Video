# Desenvolva um programa que pergunte a distância da viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km 
# e R$0,45 para viagens mais longas

num = float(input("A viagem será de quantos km? "))

if num <= 200:
    print(f"A passagem custará R${num * 0.5:.2f}! Foi aplicado 50 centavos por km")
else:
    print(f"A passagem custará R${num * 0.45:.2f}! Foi aplicado 45 centavos por Km")
