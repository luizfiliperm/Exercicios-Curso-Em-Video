# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ela ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

birthYear = int(input("Em que ano você nasceu? "))
age = int(date.today().year) - birthYear

if age < 18:
    print(f"Você ira se alistar ao serviço militar daqui a {18 - age} ano(s)!")
elif age == 18:
    print(f"Você já tem {age} anos! Está na hora de se alistar ao serviço militar!")
elif age > 18:
    print(f"Você já tem mais do que 18 anos, você deveria ter se alistado ao serviço militar {age - 18} ano(s) atrás!")
else:
    print("Ano ínvalido")
