# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
# 1 - Binário
# 2 - Octal
# 3 - Hexadecimal

num = int(input("Digite um número: "))

print(f"Você deseja converter '{num}' para qual base de conversão?")

option = int(input("1 - Binário\n2 - Octal\n3 - Hexadecimal\n4 - Todos\n"))

if option == 1 or option == 4:
    print(f"{num} em Binário é igual a: {bin(num)[2:]}")
if option == 2 or option == 4:
    print(f"{num} em Octal é igual a: {oct(num)[2:]}")
if option == 3 or option == 4:
    print(f"{num} em Hexadecimal é igual a: {hex(num)[2:]}")
if option !=  1 and option != 2 and option != 3 and option !=4:
    print("Opção Inválida")
