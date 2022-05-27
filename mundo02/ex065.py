# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores

resposta = "S"
valor = 0
maior = 0
menor = 0
count = 0
soma = 0
print("=" * 30)
while resposta == "S":
    valor = int(input("Digite um valor: "))
    if count == 0:
        menor = valor
        maior = valor

    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

    soma += valor
    count += 1
    resposta = str(input("Continuar a digitar valores [S/N]?")).strip().upper()
    print("=" * 30)

print(f"A média desses valores foi: {soma/count:.1f}")
if maior == menor:
    print("Não existe um valor maior ou menor que o outro, todos são iguais!")
else:
    print(f"O maior deles foi {maior} e o menor foi {menor}!")
