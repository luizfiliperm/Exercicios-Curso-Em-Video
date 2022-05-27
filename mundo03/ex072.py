# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numExtenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")


while True:
    count = 0
    num = -1
    while num > 20 or num < 0:
        if count > 0:
            print("Opção Inválida")
        num = int(input("Deseja mostrar qual número por extenso entre 0 e 20? "))
        count += 1
    print(numExtenso[num])
    escolha = str(input("Deseja mostrar outro número[s/n]? ")).strip().lower()
    if escolha == "n":
        break
