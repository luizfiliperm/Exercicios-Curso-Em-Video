# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indiciando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

from datetime import date


def voto(nascimento):
    idade = date.today().year - nascimento
    if 16 < idade < 18 or idade > 65:
        return(f"Com {idade} anos: VOTO OPCIONAL")
    elif idade >=18:
        return(f"Com {idade} anos: VOTO OBRIGATÓRIO")
    elif idade < 16:
        return(f"Com {idade} anos: NÃO VOTA")


ano_nascimento = int(input("Ano de Nascimento: "))
resposta = voto(ano_nascimento)
print(resposta)
