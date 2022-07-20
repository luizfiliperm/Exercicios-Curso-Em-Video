""" 
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, no final, mostre:

A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves 
"""

pessoa = list()
grupo = list()

while True:
    # Recebe os dados
    pessoa.append(str(input("Nome: ")).strip().capitalize())
    pessoa.append(int(input("Peso: ")))
    # Passa os dados para a lista
    grupo.append(pessoa[:])
    pessoa.clear()

    # Checka se quer ou nao continuar
    c = str(input("Deseja continuar?[S/N] ")).strip().upper()
    if c[0] == 'N':
        break
print("=-=" * 30)
# Quantas pessoas foram cadastradas
print(f'Foram cadastradas {len(grupo)} pessoas')

# Pessoas mais pesadas/leves

# Checka qual o maior/menor peso
c = 0
for pessoa,peso in grupo:
    
    if c == 0:
        maispesada = peso
        maisleve = peso

    if peso > maispesada:
        maispesada = peso
    if peso < maisleve:
        maisleve = peso
    c +=1

# Checka se todas as pessoas tem o mesmo peso
if maispesada == maisleve:
    print("Todas as pessoas cadastradas tem o mesmo peso")
else:
    # Imprime na tela as mais pesadas
    print(f"As pessoas mais pesadas tem o peso de {maispesada}kg e são:", end=' ')
    for p in grupo:
        if p[1] == maispesada:
            print(f"{p[0]}", end=' ')

    # Imprime na tela as mais leves
    print(f"\nAs pessoas mais leves tem o peso de {maisleve}kg e são:", end=' ')
    for p in grupo:
        if p[1] == maisleve:
            print(f"{p[0]}", end=' ')
