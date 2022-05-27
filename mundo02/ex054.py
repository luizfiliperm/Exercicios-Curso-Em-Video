# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

countMais21 = 0
countMenor21 = 0
ano = int(date.today().year)

for c in range(0, 7):
    age = int(input(f"Em que ano a {c + 1}° pessoa nasceu: "))
    age = ano - age
    if age >= 21:
        countMais21 += 1
    if age < 21:
        countMenor21 += 1

print(f"Dessas pessoas, {countMais21} já são de maior e {countMenor21} ainda não atingiram a maioridade!")