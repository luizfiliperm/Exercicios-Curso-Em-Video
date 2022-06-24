# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adcionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente.

num = []

while True:
    num2 = int(input("Digite um número: "))
    if num2 not in num:
        num.append(num2)
        print("Valor adcionado com Sucesso...")
    else:
        print("Valor duplicado! Não vou adcionar...")

    while True: 
        resposta = str(input("Deseja continuar?[S/n]: ")).strip().upper()
        if resposta[0] not in 'SN':
            print("Resposta inválida, favor digitar novamente")
        else:
            break
    if resposta[0] == 'N':    
        break

num.sort()
print("Números digitados em ordem crescente: ")
for i in num:
    print(i)
