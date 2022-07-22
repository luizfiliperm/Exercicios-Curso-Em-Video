# Aprimore o  DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

aproveitamento = dict()
gols = list()
geral = list()

while True:
    aproveitamento['Nome'] = str(input("Nome do jogador: ").strip().capitalize())
    n_partidas = int(input(f"Quantidade de partidas de {aproveitamento['Nome']}: "))

    for c in range(0, n_partidas):
        gols.append(int(input(f"Gols na partida {c + 1}: ")))

    aproveitamento['Gols'] = (gols[:])
    aproveitamento['Total'] = (sum(gols))
    gols.clear()

    geral.append(aproveitamento.copy())
    continuar = str(input("Deseja continuar? [S/N]").strip().upper())
    if continuar[0] == 'N':
        break

print("==" * 50)
print(f"Cod Nome            Gols          Total")

for e,i in enumerate(geral):
    print(f"{e:<3}", end='')
    print(f"{i['Nome']:<20}", end='')
    print(f"{i['Gols']}", end='')
    print(f"{i['Total']:>10}")
print("==" * 50)

while True:
    opcao = int(input("Deseja ver os dados de qual jogador?[999 para cancelar] "))
    if opcao == 999:
        print("Encerrado!")
        print("==" * 50)
        break
    if opcao < 0 or opcao >= len(geral):
        print("Opção Inválida, favor digitar outra!")
    else:
        print(f"Levantamento do jogador {geral[opcao]['Nome']}")
        for i in range(0, len(geral[opcao]['Gols'])):
            print(f"Na partida {i + 1}, fez {geral[opcao]['Gols'][i]} ")
    print("==" * 50)
