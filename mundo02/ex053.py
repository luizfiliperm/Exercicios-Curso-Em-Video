# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

# Recebendo a frase
frase = str(input("Digite uma frase: ").upper())

# Removendo os espaços
frase = frase.replace(" ", "")

# Checa se é um palíndromo
print(f"{frase} ao contrário é: {(frase)[::-1]}")
if frase == (frase)[::-1]:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo!")
