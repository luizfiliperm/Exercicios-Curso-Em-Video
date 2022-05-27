# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com sua idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SENIOR
# - Acima: MASTER

from datetime import date

birthYear = int(input("Em que ano você nasceu? "))
age = int(date.today().year) - birthYear

print(f"Você tem {age} anos, portanto, se enquadra na categoria ", end="")

if age <= 9:
    print("MIRIM!")
elif age <= 14:
    print("INFANTIL!")
elif age <= 19:
    print("JUNIOR!")
elif age <= 20:
    print("SENIOR!")
else:
    print("MASTER!")
    