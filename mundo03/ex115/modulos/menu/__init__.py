def opcao(msg):

    while True:
        try:
            op = int(input(msg))
        except:
            print("Opção Inválida, por favor tente novamente!")
        else:
            if op > 3 or op < 1:
                print("Opção Inválida, por favor tente novamente!")
            else:
                break
    return op


def menu():
    print('-' * 50)
    print(f'{"MENU PRINCIPAL":^50}')
    print('-' * 50)
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova Pessoa")
    print("3 - Sair do Sistema")
    print('-' * 50)
    op = opcao("Sua Opção: ")
    return op