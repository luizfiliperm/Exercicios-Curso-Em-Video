# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

ang = float(
    input("Você deseja saber o Seno, Cosseno e Tangente de qual Ângulo? "))

angrad = math.radians(ang)

print(f"O Seno de {ang} é {math.sin(angrad):.2f}\no Cosseno é {math.cos(angrad):.2f}\ne a tangente é {math.tan(angrad):.2f}")
