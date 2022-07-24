# Faça um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome_jogador = '<desconhecido>', num_gols = 0):
    print(f"O jogador {nome_jogador} fez {num_gols} gols no campeonato.")

nome = str(input("Nome do jogador: ").strip().capitalize())
gols = str(input("Número de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == '':
    ficha(num_gols=gols)
else:
    ficha(nome, gols)

