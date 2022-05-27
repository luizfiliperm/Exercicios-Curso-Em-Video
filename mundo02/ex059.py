# Crie um programa que leia dois valores e mostre um menu na tela
# [1] - Somar
# [2] - Multiplicar
# [3] - Maior
# [4] - Novos números
# [5] - Sair do Programa

from time import sleep
# Definindo variávieis
opcao = 6 # Opcao = 6 porque o máximo é 5
num1 = 0
num2 = 0
count = 0
print("=" * 30)

while opcao != 5:
    opcao = 6
    # Recebendo os valores
    num1 = int(input("Primeiro número: "))
    num2 = int(input("Segundo número: "))
    print("=" * 35)
# Opcao != e opcao != porque se for isso, vai ser desse loop, ou para fechar o programa ou para digitar novos números
    while opcao != 4 and opcao != 5: 
    # Recebendo qual função será realizada
        print(f"O que desejas fazer com {num1} e {num2}?")
        opcao = int(input("[1] - Somar\n[2] - Multiplicar\n[3] - Mostrar qual é o maior\n[4] - Digitar novos números\n[5] - Sair do programa\n"))
        print("=" * 35)
# Funções:
        # Somar os dois números
        if opcao == 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        # Multiplicar os dois números
        elif opcao == 2:
            print(f"{num1} x {num2} = {num1 * num2}")
        # Mostrar qual é o maior
        elif opcao == 3:
            if num1 > num2:
                print(f"{num1} é maior que {num2}")
            elif num2 > num1:
                print(f"{num2} é maior que {num1}")
            else:
                print("Os dois números são iguais")
        # Digitar novos números
        elif opcao == 4:
            print("Digitar novos números...")
        # Finalizar o programa
        elif opcao == 5:
            print("Finalizando...")
        # Opção Ínvalida
        else:
            print("Opção Ínvalida! Digite novamente!")  
        print("=" * 35)
        # Tempo para ver a resposta
        sleep(2)
        