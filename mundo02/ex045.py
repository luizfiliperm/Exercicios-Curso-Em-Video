# Crie um programa que faça o computador jogar Jokenpo com você
from random import choice

print("-=-" * 20)
# Começo do programa
print("Vamos jogar Jokenpô!")

# Computador escolhendo o que vai jogar
pcChoise = choice(["pedra", "papel", "tesoura"])


# Usuário escolhendo o que vai jogar
print("\nEscolhi o que vou jogar já, você vai jogar o quê? ")
uChoice = int(input("\n1 - Pedra\n2 - Papel\n3 - Tesoura\n"))

choice = ["pedra", "papel", "tesoura"]

# Jogada Ínvalida
if uChoice > 3 or uChoice < 0:
    print("Jogada Inválida")
    print("-=-" * 20)
    exit()
    
uChoice = choice[uChoice - 1]

print("-=-" * 20)

# Resultado
print(f"Eu escolhi {pcChoise} e você {uChoice}!")

if (pcChoise == "pedra" and uChoice == "tesoura") or (pcChoise == "papel" and uChoice == "pedra") or (pcChoise == "tesoura" and uChoice == "papel"):
    print("Não foi dessa vez, eu ganhei!")
elif (uChoice == "pedra" and pcChoise == "tesoura") or (uChoice == "papel" and pcChoise == "pedra") or (uChoice == "tesoura" and pcChoise == "papel"):
    print("Parabéns, você ganhou!")
else:
    print("Empate!")

print("-=-" * 20)
