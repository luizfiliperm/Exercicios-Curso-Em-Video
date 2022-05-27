# Crie um programa que crie uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.00, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livros", 34.90)

print("-" * 60)
print(f"{'Listagem de Preços'.upper() : ^60}")
print("-" * 60)

for i in range(0, len(listagem), 2):
    print(f"{listagem[i]}", end=f"{'.' * (50 - len(listagem[i]))}R${f'{listagem[i + 1]:.2f}': >8}\n")
print("-" * 60)
