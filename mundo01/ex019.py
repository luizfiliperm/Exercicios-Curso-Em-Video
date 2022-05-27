# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude a ele, lendo o nome deles e escrevendo o nome escolhido.
from random import choice

al1 = input("Qual o nome do primeiro aluno? ")
al2 = input("Qual o nome do segundo aluno? ")
al3 = input("Qual o nome do terceiro aluno? ")
al4 = input("Qual o nome do quarto aluno? ")

print(f"O escolhido foi: {choice([al1, al2, al3, al4])}")
