# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaint(string):
    while True:
        num = str(input(string))
        if num.isnumeric():
            break
        else:
            print("ERRO! Digite um número inteiro válido")
    return int(num)

n = leiaint("Digite um número: ")
print(f"Você digitou o número: {n}")
