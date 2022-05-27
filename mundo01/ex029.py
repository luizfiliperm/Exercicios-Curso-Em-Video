# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$07,00 por cada Km acima do limite

num = int(input("O carro passou a quantos km/h? "))

if num > 80:
    print(f"O carro passou a {num}km/h, acima do limite. Portanto a multa vai custar R${(num-80) * 7},00!")
else:
    print("O carro não ultrapassou o limite de velocidade! Pode seguir viagem!")