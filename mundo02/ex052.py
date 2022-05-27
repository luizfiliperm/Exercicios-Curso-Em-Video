# Faça um programa que leia um número inteiro e diga se ele é ou não um número inteiro

# num = int(input("Digite um número: "))

for c in range(0, 15):
    num = int(input("Digite um número: "))
    if num == 2 or num == 3 or num == 5 or num == 7:
        print(f"{num} é um número primo!")
    elif num == 1 or num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print(f"{num} não é um número primo!")
    else:
        print(f"{num} é um número primo!")
        