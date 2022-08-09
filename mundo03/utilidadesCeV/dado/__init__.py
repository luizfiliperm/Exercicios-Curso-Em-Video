def leiadinheiro(msg):
    valido = False
    while not valido:
        num = str(input(msg)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f"'{num}' é ínvalido, favor digitar novamente")
        else:
            valido = True
            return float(num)

