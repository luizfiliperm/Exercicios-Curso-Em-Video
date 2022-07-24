# Faça um programa que tenha uma função notas() de alunos e vai retornar um dicionário com as seguintes informações: - Quantidade de notas - A maior nota - A menor nota - A média da turma - A situação(opcional) Adcione também as docstrings da função.

def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    grade = dict()
    grade['total'] = len(notas)
    grade['maior'] = max(notas)
    grade['menor'] = min(notas)
    grade['média'] = sum(notas)/len(notas)
    if sit == True:
        if grade['média'] >= 7:
            grade['situação'] = 'BOA'
        elif 6 <= grade['média'] < 7:
            grade['situação'] = 'RAZOÁVEL'
        elif grade['média'] < 6:
            grade['situação'] = 'RUIM'
    return grade


resp = notas(3.5,2, 2, 10, 6.5, sit=True)
print(resp)
help(notas)