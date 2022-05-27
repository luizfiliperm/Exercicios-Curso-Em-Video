# Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome
nome = str(input("Digite seu nome: ")).strip().lower().title().split()
print(f"Seu nome tem 'Silva' no nome: {'Silva' in nome}")
