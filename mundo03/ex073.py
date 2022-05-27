# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética
# D) Em que posição da tabela está o time de Cuiabá.

tabela = ("Corinthias", "Atlético-MG", "São Paulo", "Botafogo", "Santos", "Coritiba", "Avaí", "América-MG", "Palmeiras", "Bragantino", "Internacional", "Fluminense", "Goiás", "Cuiabá", "Athletico-PR", "Flamengo", "Juventude", "Ceará", "Atlético-GO", "Fortaleza")

print("=-=" * 10)

# Exibe a tabela inteira
print("Tabela Brasileirão:")
for i in range (0, len(tabela)):
    print(f"{i + 1}° - {tabela[i]}")

print("=-=" * 10)

# Exibe os 5 primeiros colocados
print("5 primeiros colocados:")
for i in range (0, 5):
    print(f"{i + 1}° - {tabela[i]}")

print("=-=" * 10)

# Exibe os 4 últimos colocaods
print("4 últimos colocados:")
for i in range(-1, -5, -1):
    print(f"{len(tabela) + i + 1}° - {tabela[i]}")
print("=-=" * 10)

# Exibe os times em ordem Alfabética
print("Times em Ordem Alfabética:")
ordem = (sorted(tabela))
for i in range(0, len(ordem)):
    print(f"{ordem[i]} ",end='')
print("\n")
print("=-=" * 10)

# Exibe a posição de Cuiabá
print(f"Cuiabá está na posição {tabela.index('Cuiabá') + 1}")
print("=-=" * 10)
