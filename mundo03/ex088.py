# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

num_palpites = int(input("Quantidade de jogos que deseja gerar da MEGA SENA: "))
rand_numbers = list()
jogos_mega_sena = list()

print("Gerando números...")
sleep(1.5)
for c in range(0, num_palpites):
    for i in range(0, 6):
        while True:
            num = randint(1,60)
            if num not in rand_numbers:
                rand_numbers.append(num)
                break
    rand_numbers.sort()
    jogos_mega_sena.append(rand_numbers[:])
    rand_numbers.clear()

for i in range(0, len(jogos_mega_sena)):
    print("=-=" * 30)
    print(f"{i + 1}º jogo: {jogos_mega_sena[i]}")
    sleep(1)
print("=-=" * 30)