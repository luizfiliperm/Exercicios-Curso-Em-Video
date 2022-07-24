# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(num = 1, show=False):
    """
    - > Exibe o fatorial de um número
    :para num: O número a ser calculado
    :para show: (opcinal) Mostrar ou não a conta
    :return: O valor do fatorial de um número num
    """
    f = 1
    mostrar = ""
    for c in range(num, 0, -1):
        f *= c
        if c == num:
            mostrar += str(f"{c}")
        else:
            mostrar += str(f" x {c}")
        if c == 1:
            mostrar += str(f" = {f}")
    if show:
        return mostrar
    else:
        return f


print(fatorial(5, False))
help(fatorial)
