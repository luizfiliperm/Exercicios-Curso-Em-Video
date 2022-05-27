# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

num = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão dessa PA: "))

print("10 primeiros termos dessa PA: ")
for c in range(0, 10):
    print(f"{num} ", end=" ")
    num += razao