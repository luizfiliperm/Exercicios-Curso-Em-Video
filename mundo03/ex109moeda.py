def moeda(n):
    f = str(f"R${n:.2f}")
    return f


def aumentar(n, format = False):
    n += 10 * n/100

    if format:
        n = moeda(n)
    return n

    
def diminuir(n, format = False):
    n -= 13 * n/100
    if format:
        n = moeda(n)
    return n



def dobro(n, format = False):
    n *= 2
    if format:
        n = moeda(n)
    return n


def metade(n, format = False):
    n /= 2
    if format:
        n = moeda(n)
    return n
