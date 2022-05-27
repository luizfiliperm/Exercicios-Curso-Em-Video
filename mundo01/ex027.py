# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = str(input("Qual o seu nome completo?")).strip()
nomesplitado = nome.split()
print(f"Seu primeiro nome: {nomesplitado[0]}")
print(f"Seu último nome: {nomesplitado[-1]}")

# Outra forma de fazer:
# print(f"Seu último nome: {nomesplitado.pop()}")