# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) A Média de idade do grupo. C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas acima da média

lista_pessoas = list()
pessoa = dict()

while True:
    pessoa["Nome"] = str(input("Nome: ").strip().capitalize())
    pessoa["Sexo"] = (str(input("Sexo[M/F]: "))[0]).strip().upper()
    pessoa['Idade'] = int(input("Idade: "))
    lista_pessoas.append(pessoa.copy())

    continuar = str(input("Deseja continuar? [S/N]: ").strip().upper())
    if continuar == 'N':
        break

media = 0

for i in lista_pessoas:
    media += i['Idade']
media = media/len(lista_pessoas)

print('=' * 50)
print(f"Foram cadastradas {len(lista_pessoas)} pessoas!")
print(f"A média de idade do grupo é {media}")

print("Lista de mulheres: ")
for i in lista_pessoas:
    if i['Sexo'] == 'F':
        print(f'° {i["Nome"]}')

print("Lista de pessoas acima da média: ")
for i in lista_pessoas:
    if i['Idade'] > media:
        print(f'° {i["Nome"]} com {i["Idade"]} anos')
