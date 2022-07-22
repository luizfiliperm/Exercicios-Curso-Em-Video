# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros, inicio, fim e passo e realize a contagem. Seu programa tem que realizar 3 contagens através da função criada: a) de 1 até 10, de 1 em 1. b) de 10 até 0, de 2 em 2 c) uma contagem personalizada


from time import sleep


def contador():
    for a in range(0, 3):
        if a == 0:
            i = 1
            f = 10 + 1
            p = 1
        elif a == 1:
            i = 10
            f = 0 - 1
            p = -2
        elif a == 2:
            print("Sua vez de Personalizar a contagem!")
            i = int(input("Início: "))
            f = int(input("Fim: "))
            p = abs(int(input("Passo: ")))
            if p == 0:
                p = 1
            if f < i:
                p *= -1
                f -= 1
            elif i > f:
                f += 1
        print("*" * 10)
        
        for c in range(i, f, p):
            print(c)
            sleep(0.5)
        print("FIM!")


contador()