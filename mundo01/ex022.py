# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maíusculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo sem contar os espaços
# Quantas letras tem o primeiro nome

nomecompleto = str(input("Qual o seu nome completo? ")).strip
print(f" Seu nome em maísculo:{nomecompleto.upper()}")
print(f"Seu nome em minúsculo: {nomecompleto.lower()}")


print(f"Seu nome completo tem {len(nomecompleto.replace('', ''))} letras")

nome = nomecompleto.split()
print(f"Seu primeiro nome tem {len(nome[0])} letras")
