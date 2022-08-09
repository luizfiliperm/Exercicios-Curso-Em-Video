# Crie um módulo chamado moeda.py que tenha as funções Incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esses módulo e use algumas dessas funções

from ex107moeda import *

p = float(input("Digite o preço: R$"))

print(f"A metade de {p} é {metade(p)}")
print(f"O dobro de {p} é {dobro(p)}")
print(f"Aumentando 10%, temos {aumentar(p)}")
print(f"Diminuindo 13% temos {diminuir(p)}")
