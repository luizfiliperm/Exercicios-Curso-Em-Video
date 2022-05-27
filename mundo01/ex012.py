# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

num = float(input("Qual o preço do produto? R$"))
print(f"Seu novo preço, com 5% de desconto será: R${num - num * 5/100:.2f}")
