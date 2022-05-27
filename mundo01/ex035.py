# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print("Qual o tamanho dos lados do triângulo? ")
lado1 = int(input("lado 1: "))
lado2 = int(input("lado 2: "))
lado3 = int(input("lado 3: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("É possível formar este triângulo!")
else:
    print("Não é possível formar este triângulo!")