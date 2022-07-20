# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
num = list()
matriz = list()
for c in range(0, 3):
    for i in range(0, 3):
        num.append(int(input(f"Digite um valor para [{c},{i}]: ")))
    matriz.append(num[:])
    num.clear()

print("=-=" * 30)

for c in range(0,3):
    for i in range(0,3):
        print(f"[ {matriz[c][i]} ]", end=' ')
    print("\n")