# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantia de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado

days = float(input("O carro foi alugado por quantos dias? "))
km = float(input("O carro rodou quantos km? "))

print(f"O preço a ser pago será: R${(days * 60) + (km * 0.15):.2f}")
