# Crie um programa que vai ler vários números e colocar em uma lista, e depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores ordenadas em forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista

lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    while True:
        resposta = str(input("Deseja continuar?[S/n]")).strip().upper()
        if resposta in 'SN':
            break
        else:
            print('Resposta Inválida, favor digitar novamente!')
    if resposta == 'N':
        break

print(f"Foram digitados {len(lista)} números!")
lista.sort(reverse=True)
print(f"Números digitados em ordem decrescente: {lista}")
if 5 in lista:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")
