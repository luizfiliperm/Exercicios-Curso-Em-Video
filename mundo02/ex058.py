# Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram nescessários para vencer.

from random import randint
num = int(randint(1,100))
numjogador = 101
count = 0

print("Pensei em um número entre 1 e 100, tente advinhá-lo!(Vou dando dicas)")
while numjogador != num:
    count += 1
    numjogador = int(input(f"{count}° tentativa: "))
    if numjogador > num:
        print(f"O número que pensei é menor que {numjogador}!")
    if numjogador < num:
        print(f"O número que pensei é maior que {numjogador}!")

print(f"Parabéns, eu estava pensando no {num}! Você acertou em {count} tentavias!")
