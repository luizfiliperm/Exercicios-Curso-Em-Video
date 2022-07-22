# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela!

aluno = dict()

aluno['Nome'] = str(input("Nome do aluno: ").strip().capitalize())

aluno['Média'] = float(input(f"Média do {aluno['Nome']}: "))

if aluno['Média'] < 7:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f"{k}: {v}")