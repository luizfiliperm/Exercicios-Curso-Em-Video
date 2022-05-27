# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Qual a cidade voce nasceu? ')).strip().title().split()
print(f"A cidade começa com Santo: {cidade[0] == 'Santo'}")