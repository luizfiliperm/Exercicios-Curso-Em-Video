# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle


al1 = input("Digite o primeiro aluno para ser sorteada a ordem: ")
al2 = input("Segundo: ")
al3 = input("Terceiro: ")
al4 = input("Quarto: ")

lista = [al1, al2, al3, al4]

shuffle(lista)

print(
    f"Ordem de Apresentação:\n1- {lista[0]}\n2- {lista[1]}\n3- {lista[2]}\n4- {lista[3]}")
