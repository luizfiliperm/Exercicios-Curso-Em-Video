# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre em um boletim contendo a média de cada um e permita que o usuário possa mostras as notas de cada aluno individualmente.

notas = list()
boletim = list()
while True:
    nome = str(input("Nome: ").capitalize())
    for c in range(0, 2):
        notas.append(float(input(f"Nota {c + 1}: ")))
    boletim.append([nome, notas[:]])
    notas.clear()
    continuar = str(input("Deseja continuar? [s/n]: ").strip().lower())
    if continuar[0] == 'n':
        break
print("-" * 40)
print("NO. NOME            MÉDIA")
for c in range(0, len(boletim)):
    media = sum(boletim[c][1])/2
    print(f"{c:<1} {boletim[c][0]:^7} {media:>15}")
print("-" * 40)

while True:
    mostrar_notas = int(input("Deseja ver notas de qual aluno?(999 interromope): "))
    if mostrar_notas >= len(boletim) and mostrar_notas < 999 or mostrar_notas < 0:
        print("Aluno Inválido, favor digitar novamente!")
        print("-" * 40)
    elif mostrar_notas == 999:
        break
    else:
        print(f"As notas de {boletim[mostrar_notas][0]} são: {boletim[mostrar_notas][1]}")
        print("-" * 40)