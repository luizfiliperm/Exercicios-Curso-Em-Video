# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e os valores ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = list()
for c in range(0, 2):
    numeros.append([])
for c in range(1, 8):
    num = int(input(f"Digite o {c}º número: "))
    if num % 2 == 0 and num != 0:
        numeros[0].append(num)
    elif num % 2 != 0:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print(f"Números pares digitados:{numeros[0]}")

print(f"Números ímpares digitados:{numeros[1]}")
