def moeda(n):
    f = str(f"R${n:.2f}")
    return f


def aumentar(n):
    n += 10 * n/100
    n = moeda(n)
    return n

    
def diminuir(n):
    n -= 13 * n/100
    n = moeda(n)
    return n



def dobro(n):
    n *= 2
    n = moeda(n)
    return n


def metade(n):
    n /= 2
    n = moeda(n)
    return n