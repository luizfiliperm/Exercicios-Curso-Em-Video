# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual o nome do produto mais barato.

preçoTotal = 0
mais1k = 0
maisBarato = 0

count = 0
while True:
    print("=-=" * 10)
    nomeProduto = str(input("Nome do produto: "))
    preçoProduto = int(input("Preço do produto: R$"))
    preçoTotal += preçoProduto
    count += 1
    if preçoProduto > 1000:
        mais1k += 1
    if count == 1:
        maisBarato = preçoProduto
        maisBaratonome = nomeProduto
    elif preçoProduto < maisBarato:
        maisBarato = preçoProduto
        maisBaratonome = nomeProduto
    while True:
        continuar = str(input("Deseja continuar[S/N]? ")).strip().upper()
        if continuar in "SsNn":
            break
    if continuar == "N":
        break
    
print("=-=" * 10)
print(f"Total gasto na compra: R${preçoTotal:.2f}")
print(f"{mais1k} produtos custam mais de R$1000.00")
print(f"Nome do produto mais barato: '{maisBaratonome}', que custou R${maisBarato:.2f}")
print("=-=" * 10)
