# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo (ex035)
# E mostre qual tipo de triângulo será formado se for possível formar um triângulo
# - Equilátero: Todos os lados iguais
# - Isóceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes

print("Qual o tamanho dos lados do triângulo?")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("É possível formar um triângulo ", end="")
    if lado1 == lado2 == lado3:
        print("equilátero!")
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print("isóceles!")
    else:
        print("escaleno!")
else:
    print("Não é possível formar um triângulo!") 
