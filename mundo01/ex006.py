# Crie um algorítimo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.

num = int(
    input("Digite um número para eu mostrar seu dobro, triplo e a raiz quadrada: "))

print(
    f"Dobro == {num * 2}\nTriplo == {num * 3}\nRaiz quadrada == {num ** (1/2):.2f}")
