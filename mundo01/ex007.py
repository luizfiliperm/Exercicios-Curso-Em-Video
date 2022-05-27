# Desenvolva um programa que leia duas notas, calcule e mostre sua média

from tkinter.tix import InputOnly


nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

print(f"A média do aluno foi: {(nota1 + nota2)/2:.1f}")
