# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado(valor inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possúi cédulas de R$50, R$20, R$10 e R$1

valor = int(input("Valor a ser sacado: R$"))

nota100 = valor // 100
valor = valor % 100
nota50 = valor // 50
valor = valor % 50
nota20 = valor // 20
valor = valor % 20
nota10 = valor // 10
valor = valor % 10
nota01 = valor


if nota100 > 0:
    print(f"{nota100} notas de R$100")
if nota50 > 0:
    print(f"{nota50} notas de R$50")
if nota20 > 0:
    print(f"{nota20} notas de R$20")
if nota10 > 0:
    print(f"{nota10} notas de R$10")
if nota01 > 0:
    print(f"{nota01} notas de R$1")
