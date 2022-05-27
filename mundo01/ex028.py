# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0  e 5 e peça para o usuário tentar advinhar
# qual número foi escolhido pelo computador, o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

print("Vou pensar em um número entre 0 e 5 e quero que você tente advinhar qual é esse número!")
num = randint(0,5)
SugestedNumber = int(input("Pronto, em qual número eu pensei? "))

if SugestedNumber == num:
    print(f"Parabéns, eu pensei no {num}! Você acertou!")
else:
    print(f"Não foi dessa vez, você errou! Eu pensei no {num}!")