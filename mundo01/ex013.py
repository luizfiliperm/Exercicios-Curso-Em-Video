# Faça um algorítimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

num = float(input("Qual o salário do funcionário? R$"))

print(
    f"Seu novo salário, com 15% de aumento será de:R${num + num * 15/100:.2f}")
