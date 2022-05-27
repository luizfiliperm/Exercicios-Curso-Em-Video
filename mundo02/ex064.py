# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag)

num = 0
count = 0
soma = 0
while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        count += 1
        soma += num
        

print(f"Foram digitados {count} números e a soma entre eles é {soma}")
