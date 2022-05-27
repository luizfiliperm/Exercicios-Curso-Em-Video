# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa
from math import hypot

cat1 = float(input("Qual o valor do cateto 1 do Triângulo Retângulo? "))
cat2 = float(input("E o cateto 2? "))

print(f"A hipotenusa desse triângulo  vale {hypot(cat1, cat2)}")
