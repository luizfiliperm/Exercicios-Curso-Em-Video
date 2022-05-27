# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

# Recebe os valores (nome do comprador), (valor da casa), (em quantos anos será pago), (salário do comprador)

print("-=-" * 20)
name = str(input("Qual o seu nome? "))
housevalue = float(input(f"Olá {name}, qual o valor da casa que desejas comprar? "))
installments = int(input("Em quantos anos você gostaria de pagar a casa? ")) * 12
wage = float(input(f"{name}, última pergunta, qual o seu salário mensal? "))
print("-=-" * 20)
# Calcula o valor da prestação mensal
installmentVallue = housevalue/installments 

# Condições: Não pode exceder 30% do salário do comprador
print("-=-" * 20)
if installmentVallue <= 30/100 * wage:
    print(f"Então {name}, está tudo certo para o empréstimo acontecer, estarei realizando os próximos passos!")
    print(f"As parcelas mensais serão de R${installmentVallue:.2f}")
    print(f"Você pagará elas em {installments} meses")
elif installmentVallue > 30/100 * wage:
    print(f"Então {name}, infelizmente não será possível concluir o empréstimo, você não cumpriu os requisitos nescessários!")
else:
    print("Algum erro ocorreu!")