# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

sorteados = (randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))

print("Números sorteados:")
for i in range(0, len(sorteados)):
    print(sorteados[i])
print(f"O menor valor sorteado foi: {sorted(sorteados)[0]}")
print(f"E o maior valor sorteado foi: {sorted(sorteados)[-1]}")
