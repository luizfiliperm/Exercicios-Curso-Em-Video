# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior número!")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior número!")
elif num3 > num1 and num3 > num2:
    print(f"{num3} é o maoir número!")
else:
    print("Não existe um número dentre estees que você mandou que é maior que os outros dois!")

if num1 < num2 and num1 < num3:
    print(f"{num1} é o menor número")
elif num2 < num1 and num2 < num3:
    print(f"{num2} é o menor número!")
elif num3 < num1 and num3 < num2:
    print(f"{num3} é o menor número")
else:
    print("Não existe um número dentre estes que você mandou que é menor que os outros dois!")