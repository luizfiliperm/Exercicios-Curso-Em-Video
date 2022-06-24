# Faça um progama que leia 5 valores númericos e guarde-os em um lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valores = []
sorted = []
for i in range(0,5):
    valores.append(int(input(f"Digite um valor para a posição {i}: ")))

sorted = valores[:]
sorted.sort()

print(f"Maior valor digitado: {sorted[-1]}, nas posições: ", end='')
for i,c in enumerate(valores):
    if c == sorted[-1]:
        print(i, end='...')

print(f"\nMenor valor digitado: {sorted[0]}, nas posições: ", end='')

for i, c in enumerate(valores):
    if c == sorted[0]:
        print(i, end='...')
