def checkaFuncionalidade(opcao):
    if opcao == 1:
        verCadastros()
    if opcao == 2:
        cadastrar()


def cadastrar():
    print('-' * 50)
    print("Cadastrar nova pessoa")
    while True: 
        try:
            nome = str(input("Nome: ")).title().strip()
        except:
            print("Nome Inválido")
        else:
            break
    while True: 
        try:
            idade = int(input("Idade: "))
        except:
            print("Idade Inválida")
        else:
            break
    print("-" * 50)
    

    Pessoas_cadastradas = open("mundo03/ex115/Pessoas_Cadastradas.txt", "a")
    Pessoas_cadastradas.write(f"{nome}")
    ajustar = 50 - len(nome)
    Pessoas_cadastradas.write(f"{idade:>{ajustar}}\n")
    Pessoas_cadastradas.close
    print(f"Novo registro de {nome} foi adcionado!")
    return

def verCadastros():
    print("-" * 50)
    print(f"{'PESSOAS CADASTRADAS':^50}")
    print("-" * 50)
    print()
    Pessoas_cadastradas = open("mundo03/ex115/Pessoas_Cadastradas.txt", "r")
    print(Pessoas_cadastradas.read())
    Pessoas_cadastradas.close()
    return
