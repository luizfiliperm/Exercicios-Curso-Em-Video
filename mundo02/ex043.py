# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seus status de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print("Informe seu peso em kg e altura em m para eu calcular seu IMC:")
peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / altura ** 2

print(f"Seu IMC é de {imc:.2f} e você está ", end="")

if imc < 18:
    print("abaixo do peso!")
elif imc >= 18 and imc < 25:
    print("no peso ideal!")
elif imc >= 25 and imc < 30:
    print("acima do peso!")
elif imc >= 30 and imc < 40:
    print("com obesidade!")
else:
    print("com obesidade mórbida!")
    