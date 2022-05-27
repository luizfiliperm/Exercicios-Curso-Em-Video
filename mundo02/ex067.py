# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo
print("-=-" * 30)
while True:    
    num = int(input("Tabuada do : "))
    if num < 0:
        print("Finalizando o programa...")
        break
    for c in range (1, 11):
        print(f"{c} x {num} = {c * num}")
    print("-=-" * 30)
    