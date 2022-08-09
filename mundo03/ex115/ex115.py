# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

from modulos.menu import menu
from modulos.funcionalidades import checkaFuncionalidade
opcao = 1
while opcao != 3:
    opcao = menu()
    checkaFuncionalidade(opcao)
