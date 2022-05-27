# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos

# Recebendo quantas vezes a repetição ira acontecer
pessoascadastradas = int(input("Deseja cadastrar quantas pessoas? "))

# Definindo algumas variáveis
somaidade = 0
n = 0
count = 0

print("+-" * 20)

# Recebendo dados
for c in range(0, pessoascadastradas):
    nome = str(input(f"Nome da {c + 1}° pessoa: ")).strip()
    idade = int(input(f"Idade da {c + 1}° pessoa: "))
    sexo = str(input(f"Sexo da {c + 1}° pessoa[M/F]: "))

    print("+-" * 20)

# Salvando dados 

    somaidade += idade
    if sexo in "Mm" and idade > n:
        n = idade
        olderMan = str(nome)
    if sexo in "Ff" and idade < 20:
        count += 1

    
# Enviando informações
print(f"Media de idade das pessoas: {somaidade/(c + 1):.1f}")

if n == 0:
    print("Não foram registrados homens na pesquisa!")
else:
    print(f"Nome do homem mais velho: {olderMan}")

if count == 0:
    print("Não foram registradas mulheres com menos de 20 anos!")
else:  
    print(f"Quantidade de mulheres que tem menos de 20 anos: {count} ")
print("+-" * 20)
