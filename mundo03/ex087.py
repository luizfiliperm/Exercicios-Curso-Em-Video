# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

num = list()
matriz = list()
somapares = 0
somaterceiracoluna = 0
for c in range(0, 3):
    for i in range(0, 3):
        num.append(int(input(f"Digite um valor para [{c}, {i}]: ")))

        # Somando os números pares que aparecerem
        if num[-1] % 2 == 0:
            somapares += num[-1]
        # Somando os valores da terceira coluna
        if i == 2:
            somaterceiracoluna += num[-1]
    matriz.append(num[:])
    num.clear()

print("=-=" * 30)
for c in range(0,3):
    for i in range(0,3):
        print(f"[ {matriz[c][i]} ]", end=' ')
    print("\n")

print("=-=" * 30)

print(f"A soma de todos os valores pares é: {somapares}!")
print(f"A soma de todos os números da terceira coluna é: {somaterceiracoluna}")
print(f"O maior valor da segunda linha é: {max(matriz[1])}")