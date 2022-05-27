# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos

mais18 = 0
homens = 0
fmenos20 = 0

while True:
    print("=-=" * 10)
    print("Cadastre uma pessoa")
    print("=-=" * 10)

    idade = int(input("idade: "))
    while True:
        sexo = str(input("Sexo[M/F]: ")).strip().upper()
        if sexo in "MmFf":
            break
    
    if idade > 18:
        mais18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        fmenos20 += 1
    while True:
        escolha = str(input("Cadastrar mais alguém[S/N]?")).strip().upper()
        if escolha in "SN":
            break
    if escolha == "N":
        break

print(f"{mais18} pessoas são maiores de idade!")
print(f"{homens} homens foram cadastrados!")
print(f"{fmenos20} mulheres tem menos de 20 anos!")