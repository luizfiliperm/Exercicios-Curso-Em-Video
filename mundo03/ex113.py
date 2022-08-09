# Reescrava a função leitaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo ínvalido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leitaint(msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print("O usuário preferiu não informar os dados")
            return 0
        except:
            print("ERRO: por favor, digite um número inteiro válido!")
        else:
            break
    return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except KeyboardInterrupt:
            print("O usuário preferiu não informar os dados")
            return 0
        except:
            print("ERRO: por favor, digite um valor real válido!")
        else:
            break
    return num


a = leitaint("Digite um número inteiro: ")
b = leitaint("Digite um número real: ")
print(a, b)

