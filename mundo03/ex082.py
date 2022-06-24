# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das 3 listas geradas

numeros = []
pares = []
ímpares = []

while True:
    numeros.append(int(input("Digite um número: ")))

    while True:
        resposta = str(input("Deseja continuar?[S/n]").strip().lower())
        if resposta[0] in 'sn':
            break
        else:
            print("Resposta Inválida, favor digitar novamente!")
    if resposta[0] == 'n':
        break

for item in numeros:
    if item % 2 == 0:
        pares.append(item)
    elif item % 2 != 0:
        ímpares.append(item)

print(f"Lista de todos os números digitados: {numeros}")
print(f"Lista de todos os números pares digitados: {pares}")
print(f"Lista de todos os números ímpares digitados: {ímpares}")
