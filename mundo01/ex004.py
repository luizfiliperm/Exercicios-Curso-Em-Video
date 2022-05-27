# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

algo = input("Digite algo: ")

print(f"O tipo de primitivo desse valor é: {type(algo)}")
print(f"{algo} é um número: {algo.isdecimal()}")
print(f"{algo} são letras: {algo.isalpha()}")
print(f"{algo} é só espaço: {algo.isspace()}")
print(f"{algo} está em lowercase: {algo.islower()}")
print(f"{algo} está em uppercase: {algo.isupper()}")
print(f"{algo} está capitalizado: {algo.istitle()}")
