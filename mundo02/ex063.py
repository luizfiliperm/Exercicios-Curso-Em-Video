# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros números de uma sequência de Fibonacci
print("=" * 30)
print("Sequência de Fibonacci")
limite = int(input("Deseja ver quantos termos?\n"))

t1 = 0
t2 = 1
cont = 3

print("=" * (limite * 5 + 2))
if limite == 0:
    print("", end = "")
elif limite == 1:
    print(t1)
elif limite == 2:
    print(f"{t1} » {t2}", end = " » " )
    
else:
    print(f"{t1} » {t2}", end = " » " )
    while cont <= limite:

        t3 = t1 + t2
        print(f"{t3}", end = " » ")
        
        t1 = t2
        t2 = t3  
        cont += 1
print("Fim")
print("=" * (limite * 5 + 2))