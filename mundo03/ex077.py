# Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

palavras = ('padre', 'carro', 'teste', 'camisa', 'perna','computador','teclado','mouse', 'viola')

for i in range(0, len(palavras)):
    print(f"\nNa palavra {palavras[i].upper()} temos ", end='')
    for c in range(0, len(palavras[i])):
        if 'a' in palavras[i][c]:
            print("a", end=' ')
        elif 'e' in palavras[i][c]:
            print("e",end=' ')
        elif 'i' in palavras[i][c]:
            print("i",end=' ')
        elif 'o' in palavras[i][c]:
            print("o",end=' ')
        elif 'u' in palavras[i][c]:
            print("u",end=' ')
