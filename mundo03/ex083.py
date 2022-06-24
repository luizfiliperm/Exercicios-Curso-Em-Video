# Crie um programa onde o usuário digite uma expressão que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechados na ordem correta

expressão = str(input("Digite uma expressão: "))

if expressão.count('(') == expressão.count(')'):
    print("Expressão Válida!")
else:
    print("Expressão Inválida!")

# OBS: Ainda vou ajeitar esse cod