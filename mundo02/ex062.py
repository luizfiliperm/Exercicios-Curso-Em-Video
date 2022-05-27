# Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

num = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
ntermos = int(input("Quantidade de termos: "))
while ntermos != 0:
    i = 1
    print(f"{num} ", end = "")

    while i != ntermos:
        print (f"{num + razao} ", end = "")
        num += razao
        i += 1
    ntermos = int(input("\nDeseja ver mais termos? Digite a quantidade(0 para parar o programa): "))
