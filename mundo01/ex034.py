# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

num = float(input("Qual o seu salário atual? "))

if num > 1250:
    print("Você recebeu um aumento de 10%")
    print(f"Seu novo salário é de: R${num + (10/100 * num):.2f}")
else:
    print("Você recebeu um aumento de 15%")
    print(f"Seu novo salário é de: R${num + (15/100 * num):.2f}")