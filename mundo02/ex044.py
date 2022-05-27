# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print("-=-" * 20)
print("Qual produto deseja comprar?")
produto = int(input("1 - Produto 1: R$30.00\n2 - Produto 2: R$45.00\n3 - Produto 3: R$70.00\n"))

if produto == 1:
    preço = float(30)
elif produto == 2:
    preço = float(45)
elif produto == 3:
    preço = float(70)
else:
    print("Produto inválido!")

print("-=-" * 20)

print(f"Certo, você deseja comprar o produto {produto}!\nQual a forma de pagamento?")
pagamento = int(input("1 - À vista no dinheiro/cheque(10% de desconto)\n2 - À vista no cartão(5% de desconto)\n3 - 2x no cartão\n4 - 3x ou mais no cartão(20% de juros)\n"))

print("-=-" * 20)

if pagamento == 1:
    print(f"O valor será de R${preço - (preço * 10/100):.2f} pagando no dinheiro ou no cheque!")
elif pagamento == 2:
    print(f"O valor será de R${preço - (preço * 5/100):.2f} no cartão!")
elif pagamento == 3:
    print(f"O valor será de R${preço:.2f} parcelando em até 2x no cartão!")
elif pagamento == 4:
    print(f"O valor será de R${preço + (preço * 20/100)} parcelando em 3x ou mais no cartão!")
else:
    print("Pagamento Ínvalido!")
    