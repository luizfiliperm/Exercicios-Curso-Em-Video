# Faça um programa que leia um número e mostre na tela qual o seu fatorial!

# Fazendo com While
num = int(input("Digite um número: "))
fatorial = 1
print(f"{num}! = ", end = "")
while num != 1:
    print(f"{num} x ", end = "")
    fatorial *= num
    num -= 1

print(f"1 = {fatorial}")


# Fazendo com For
num = int(input("Digite um número: "))
fatorial = 1
print(f"{num}! = ", end = "")

for c in range (num, 1, -1):
    print(f"{c} x ", end = "")
    fatorial *= c

print(f"1 = {fatorial}")
