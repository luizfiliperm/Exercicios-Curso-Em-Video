# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
print("=-=" * 10)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-=" * 10)
count = 0

while True:
    while True:
        jogadorNum = input("Digite um número: ")
        check = bool(isinstance(int(jogadorNum), int))
        if check == True:
            break
            
    computadorNum = int(randint(0, 10))
    # print(computadorNum)
    while True:
        jogadorEscolha = str(input("Par ou Ímpar[P/I]: ")).strip().upper()
        if jogadorEscolha in "PpIi":
            break
    
    resultado = jogadorNum + computadorNum

    print("=-=" * 10)
    print(f"Você jogou {jogadorNum} e eu joguei {computadorNum}. Total: {resultado}!", end = " ")
    if resultado  % 2 == 0:
        print("DEU PAR!!")
    else:
        print("DEU ÍMPAR!!")

    if (jogadorEscolha == "P" and resultado % 2 == 0) or (jogadorEscolha == "I" and resultado % 2 != 0):
        print("Parabéns, você ganhou! Vamos jogar novamente!")
        print("=-=" * 10)
        count += 1
    else:
        print(f"Infelizmente você perdeu! Você ganhou {count} vezes consecutivas!")
        print("=-=" * 10)
        break
