import sqlite3
from src.Clientes import Menu_Clientes
from Faturas import criar_fatura, visualizar_faturas, editar_fatura, eliminar_fatura

print('###############################')
print('BEM VINDO Á OFICINA AUTOMOVEL!')
print('###############################')
print("\n")

# Verificar se o Utilizador já tem uma conta
registro = input('Você já tem uma conta? (S/N) ')

if registro.lower() == 's':
    utilizador = input('Digite seu nome de Utilizador: ')
    password = input('Digite sua senha: ')
    print('\n' * 2)
    print('Login realizado com sucesso!')
    print('Bem-vindo, {}! É bom vê-lo!'.format(email.title()))
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
    print("4 - Adicionar Serviço")
    print("0 - SAIR")
    opcao = input('Digite sua opção: ')

    if opcao == '0':
        print('Até breve!')
        print('Fechando o programa...')
        break
    elif opcao == '1':
        Menu_Clientes()
    elif opcao == '2':
        print('')
    elif opcao == '3':
        print("\n")
        print("###############################")
        print("#        MENU DE FATURAS       #")
        print("###############################")
        print("\n")
        print("Escolha uma opção:")
        print("1 - Criar Fatura")
        print("2 - Visualizar Faturas")
        print("3 - Editar Fatura")
        print("4 - Eliminar Fatura")
        print("0 - Voltar ao Menu Principal")
        opcao_fatura = input('Digite sua opção: ')

        if opcao_fatura == '0':
            continue
        elif opcao_fatura == '1':
            criar_fatura()
        elif opcao_fatura == '2':
            visualizar_faturas()
        elif opcao_fatura == '3':
            editar_fatura()
        elif opcao_fatura == '4':
            numero_fatura = input("Digite o número da fatura que deseja eliminar: ")
            eliminar_fatura(numero_fatura)
        else:
            print('Opção inválida. Tente novamente.')
    elif opcao == '4':
        print('')
