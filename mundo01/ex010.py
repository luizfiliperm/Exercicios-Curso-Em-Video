# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (US$100 = R$5,02) 10/03/2022

num = float(input("Quanto você tem na carteira? "))
print(f"Com R${num:.2f} você pode comprar US${num / 5.02:.2f}")
