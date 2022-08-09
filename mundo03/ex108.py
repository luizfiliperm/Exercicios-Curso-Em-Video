# Adapte o código do desafio 107, criando uma função adcional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

# Crie um módulo chamado moeda.py que tenha as funções Incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esses módulo e use algumas dessas funções

from ex108moeda import *

p = float(input("Digite o preço: R$"))

print(f"A metade de {moeda(p)} é {metade(p)}")
print(f"O dobro de {moeda(p)} é {dobro(p)}")
print(f"Aumentando 10%, temos {aumentar(p)}")
print(f"Diminuindo 13% temos {diminuir(p)}")
