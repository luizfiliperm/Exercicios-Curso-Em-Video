# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

aproveitamento = dict()
gols = list()

aproveitamento['Nome'] = str(input("Nome do jogador: ").strip().capitalize())
n_partidas = int(input(f"Quantidade de partidas de {aproveitamento['Nome']}: "))

for c in range(0, n_partidas):
    gols.append(int(input(f"Gols na partida {c + 1}: ")))

aproveitamento['Gols'] = (gols)
aproveitamento['Total'] = (sum(gols))

print("=" * 50)

for k,v in  aproveitamento.items():
    print(f"{k}: {v}")

print("=" * 50)

print(f"O jogador {aproveitamento['Nome']} jogou {len(aproveitamento['Gols'])} partidas")

for e, v in enumerate(aproveitamento['Gols']):
    print(f'{f"Na partida {e + 1}, fez {v} gols!":>27}')

print(f"Com um total de {aproveitamento['Total']} gols!")
