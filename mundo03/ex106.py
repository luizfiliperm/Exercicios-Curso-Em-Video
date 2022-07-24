# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM' o programa se encerrará.

from time import sleep


def mensagem(msg):
    num = len(msg) + 4
    print("*" * num)
    print(f"{msg:^{num}}")
    print("*" * num)

while True:
    mensagem("SISTEMA DE AJUDA PyHELP")

    funcao = str(input("Função ou Biblioteca > ").strip().lower())
    if funcao == 'fim':
        break
    mensagem(f"Acessando o manual do comando '{funcao}'")
    sleep(1)
    print(help(funcao))
    print('\n')
mensagem("Até logo")
