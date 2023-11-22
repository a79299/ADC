import sqlite3
from Clientes import Menu_Clientes
from Faturas import menu_faturas

print('###############################')
print('BEM VINDO Á OFICINA AUTOMOVEL!')
print('###############################')
print("\n")

registro = input('Você já tem uma conta? (S/N) ')

if registro.lower() == 's':
    utilizador = input('Digite seu nome de Utilizador: ')
    password = input('Digite sua senha: ')
    print('\n' * 2)
    print('Login realizado com sucesso!')
    print('Bem-vindo, {}! É bom vê-lo!'.format(utilizador.title()))
else:
    email = input('Digite seu email: ')
    password = input('Digite sua senha: ')
    print('\n' * 2)
    print('Registro concluído com sucesso!')
    print('Bem-vindo, {}! É bom vê-lo!'.format(email.title()))

while True:
    print("\n")
    print("##################################")
    print("#          MENU PRINCIPAL         #")
    print("##################################")
    print("\n")
    print("Escolha uma opção:")
    print("1 - Clientes")
    print("2 - Veiculos")
    print("3 - Faturas")
    print("0 - SAIR")
    opcao = input('Digite sua opção: ')

    if opcao == '0':
        print('Até breve!')
        print('Fechando o programa...')
        break
    elif opcao == '1':
        print('Opção de clientes escolhida')
    elif opcao == '2':
        print('Opção de veículos escolhida')
    elif opcao == '3':
        menu_faturas()
    else:
        print('Opção inválida. Tente novamente.')
