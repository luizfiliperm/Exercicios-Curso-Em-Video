# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores = dict()
print("SORTEANDO OS VALORES!")
for i in range(0,4):
    num = randint(1,6)
    jogadores[f'Jogador {i + 1}'] = num

for k,v in jogadores.items():
    sleep(1)
    print(f"O {k} tirou {v} no d6!")

jogadores = {k: v for k, v in sorted(jogadores.items(), key=lambda item: item[1], reverse=True)}

print("Ranking: ")
for e,(k,v) in enumerate(jogadores.items()):
    sleep(1)
    print(f"{e + 1}° lugar: {k} - {v}")
