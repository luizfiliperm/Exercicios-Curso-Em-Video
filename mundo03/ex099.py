# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa terá que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print("*" * 50)
    maior = 0
    for e,i in enumerate(num):
        print(i, end=" ")
        if e == 0:
            maior = i
        elif i > maior:
            maior = i

    print(f"Foram informados {len(num)} valores ao todo!")
    print(f"O maior valor informado foi: {maior}.")

    print("*" * 50)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()