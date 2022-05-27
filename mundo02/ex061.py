# Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA.
# mostrando os 10 primeiros termos da progressão utilizando a estrutura "While"

num = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
ntermos = int(input("Quantidade de termos: "))
i = 1
print(f"{num} ", end = "")

while i != ntermos:
    print (f"{num + razao} ", end = "")
    num += razao
    i += 1

