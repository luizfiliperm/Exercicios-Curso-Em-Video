# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e SomaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior

from random import randint
from time import sleep


def sorteio(lst):
    print("Sorteando 5 valores da lista:", end=" ")
    for cont in range(0, 5):
        sleep(0.5)
        rand = randint(1, 10)
        print(rand, end=" ", flush=True)
        lst.append(rand)
    print()


def SomaPar(lst):
    somapar = 0
    for i in lst:
        if i % 2 == 0:
            somapar += i

    print(f"Somando os valores pares de {lst}, temos {somapar}")


numeros = list()

sorteio(numeros)
SomaPar(numeros)