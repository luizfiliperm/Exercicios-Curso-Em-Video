# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso

n = 0
m = 0
for c in range(0, 5):
    peso = int(input(f"Peso da {c + 1}° pessoa: "))
    if c == 1:
        n = peso
        m = peso
    if peso > n:
        n = peso
    if peso < m:
        m = peso

if m == n:
    print("Todos os pesos são iguais!")
else:
    print(f"O maior peso foi de {n}kg e o menor foi de {m}kg")
