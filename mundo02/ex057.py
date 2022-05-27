# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto

# O "[0]" vai pegar apenas a primeira letra
sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

while sexo != "M" and sexo != "F":
    sexo = str(input(f"{sexo} não é uma opção! Favor digitar novamente[M/F]: ")).upper()
if sexo == "M":
    sexo = "Masculino"
else:
    sexo = "Feminino"
print(f"Sexo registrado: {sexo}!")
