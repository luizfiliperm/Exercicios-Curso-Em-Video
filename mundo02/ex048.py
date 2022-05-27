# Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500
n = 0
cont = 0
for c in range (3, 501, 6):
    cont = cont + 1 
    n = n + c
print(f"Soma de todos os números ímpares múltiplos de 3({cont}) e que se encontram no intervalo de 1 até 500 é: {n}")
