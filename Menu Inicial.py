import sqlite3
from clientes.Menu_dos_Clientes import Menu_Clientes

def adicionar_login(utilizador, password):
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()

        # Adiciona informações de login à tabela 'logins'
        cursor.execute("INSERT INTO logins (utilizador, password) VALUES (?, ?)", (utilizador, password))
        conexao.commit()
        print("Informações de login adicionadas com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao adicionar informações de login: {erro}")

    finally:
        conexao.close()

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
    print('Bem-vindo, {}! É bom vê-lo!'.format(utilizador.title()))
else:
    utilizador = input('Digite seu nome de Utilizador: ')
    password = input('Digite sua senha: ')
    adicionar_login(utilizador, password)
    print('\n' * 2)
    print('Registro concluído com sucesso!')
    print('Bem-vindo, {}! É bom vê-lo!'.format(utilizador.title()))

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
        print('O nome do ADM lindão é Daniel Sodré!')
    elif opcao == '3':
        print('O nome do ADM lindão é Daniel Sodré!')
    elif opcao == '4':
        print('O nome do ADM lindão é Daniel Sodré!')
