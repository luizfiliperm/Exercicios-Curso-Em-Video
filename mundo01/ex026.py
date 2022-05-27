# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela última vez

frase = str(input("Digite uma frase: ")).strip()

frase2 = frase.replace('á', 'a'). replace('â', 'a').replace('à', 'a').replace('ã', 'a').lower()
print(f"A frase '{frase}' possui {frase2.count('a')} letras 'a'")
print(f"A letra 'a' aparece pela primeira vez na frase: '{frase}' na posição {frase2.find('a') + 1} ")
print(f"A letra 'a' aparece pela última vez na frase: '{frase}' na posição {frase2.rfind('a') + 1}")