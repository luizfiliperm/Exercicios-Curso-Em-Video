# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

num1 = int(input("Qual a largura da sua parede? "))
num2 = int(input("Qual a altura da sua parede? "))

num3 = num1 * num2

print(f"Você precisa de {num3/2} litros de tinta para pintar sua parede")
