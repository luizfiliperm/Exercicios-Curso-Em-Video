def moeda(n):
    f = str(f"R${n:.2f}")
    return f


def aumentar(n, au , format = False):
    n += au * n/100

    if format:
        n = moeda(n)
    return n

    
def diminuir(n,di, format = False):
    n -= di * n/100
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


def resumo(n, au, di, format = True):
    a = aumentar(n, au, format)
    d = diminuir(n,di, format)
    do = dobro(n, format)
    m = metade(n, format)
    n = moeda(n)
    print(f''' 
        {"-" * 30}
        {"Resumo do valor":^30}
        {"-" * 30}
        Preço analisado: {n}
        Dobro do preço: {do}
        Metade doo preço: {m}
        {au}% de aumento: {a}
        {di}% de redução: {d}
        {"-" * 30}
    ''')