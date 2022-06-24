# Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort). 
# No final, mostre a lista ordenada na tela

num = []
for c in range(0,5):
    num2 = int(input("Digite um valor: "))
    if c == 0 or num2 >= num[-1]:
        num.append(num2)
        print("Número adcionado ao final da lista...")
    else:
        for item in num:
            if num2 <= item:
                num.insert(num.index(item), num2)
                print(f"Número adcionado na posição {num.index(num2)} da lista...")
                break
print(num)
