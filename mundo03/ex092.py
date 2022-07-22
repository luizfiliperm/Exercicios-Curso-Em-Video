# Crie um programa q leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário, se por acaso a CTPS for diferente de zero, o dicionário também receberá o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

infos =  dict()

infos['Nome'] = str(input("Digite seu nome: ").strip().capitalize())
infos['Idade'] = date.today().year - int(input("Ano de Nascimento: "))
infos['CTPS'] = int(input("Carteira de trabalho: "))

if infos['CTPS'] != 0:
    infos['Ano de Contratação'] = int(input("Ano de Contratação: "))
    infos['Anos Trabalhados'] = date.today().year - infos['Ano de Contratação']
    infos['Salário'] = str('R$') + str(input("Salário Atual: R$"))
    infos['Idade de Aposentadoria'] = infos['Idade'] + (35 - infos['Anos Trabalhados'])

print('-' * 50)

for k, v in infos.items():
    print(f'{k}: {v}')

print('-' * 50)