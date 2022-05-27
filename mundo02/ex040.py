# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7 ou superior: APROVADO

nota1 = float(input("Quanto foi sua primeira nota? "))
nota2 = float(input("Quanto foi sua segunda nota? "))

media = (nota1 + nota2) / 2

print(f"Sua média foi de {media:.2f}!")
if media < 5:
    print("Você não atingiu a média! Infelizmente, você foi REPROVADO!")
elif media >= 5 and media <= 6.9:
    print("Você não atingiu a média, porém, terá outra chance! Você está de RECUPERAÇÃO!")
else:
    print("Parabéns, sua nota foi acima da média! Você foi APROVADO!")