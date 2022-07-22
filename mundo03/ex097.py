# Faça um programa que tenha uma função escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    tam = len(txt) + 4
    print("*" * tam)
    print(f"{txt:^{tam}}")
    print("*" * tam)

escreva("oi")
escreva("MENSAGEM GRANDE AQUI")