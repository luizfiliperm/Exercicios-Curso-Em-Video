# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais , informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from ex109moeda import *

p = float(input("Digite o preço: R$"))

print(f"A metade de {moeda(p)} é {metade(p, True)}")
print(f"O dobro de {moeda(p)} é {dobro(p)}")
print(f"Aumentando 10%, temos {aumentar(p)}")
print(f"Diminuindo 13% temos {diminuir(p)}")
