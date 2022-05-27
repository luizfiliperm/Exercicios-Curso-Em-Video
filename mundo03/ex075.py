# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitada o valor 3
# C) Quais foram os números pares


numeros = (int(input("Digite o primeiro valor: ")), (int(input("Digite o segundo valor: "))), (int(input("Digite o terceiro valor: "))), (int(input("Digite o quarto valor: "))))

# Quantas vezes apareceu o valor 9:
print(f"'9' apareceu {numeros.count(9)} vezes")

# Em que posição foi digitada o valor 3:
if 3 in numeros:
    print(f"O número '3' apareceu pela primeira vez na posição: {(numeros.index(3)) + 1}")
else:
    print("Não teve número 3")

# Quais foram os números pares
print("Números pares que apareceram foram", end=" ")
count = 0
for i in range(0,4):
    if numeros[i] % 2 == 0:
        print(numeros[i], end=" ")
        count = 1
if count == 0:
    print("nenhum")
