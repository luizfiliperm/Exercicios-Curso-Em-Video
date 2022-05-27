# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o
print("Digite 6 números:")
n = 0
for c in range(0, 6):
    i = int(input(f"{c + 1}°: "))
    if i % 2 == 0:
        n = n + i
print(f"A soma apenas dos números pares que você digitou é {n}!")
