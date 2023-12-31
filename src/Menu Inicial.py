import sqlite3
from Clientes import *
from Faturas import menu_faturas

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def clientes_exists(cursor, email, password):
    """
    Verifica se o utilizador existe na base de dados.

    :param cursor: Cursor para executar consultas na base de dados.
    :type cursor: sqlite3.Cursor

    :param email: Email do utilizador.
    :type email: str

    :param password: Senha do utilizador.
    :type password: str

    :return: True se o utilizador existe, False caso contrário.
    :rtype: bool
    """
    cursor.execute("SELECT * FROM clientes WHERE email = ? AND password = ?", (email, password))
    return cursor.fetchone() is not None

print('###############################')
print('BEM VINDO À OFICINA AUTOMÓVEL!')
print('###############################')
print("\n")

registro = input('Você já tem uma conta? (S/N) ')

if registro.lower() == 's':
    utilizador = input('Digite seu nome de Utilizador: ')
    password = input('Digite sua senha: ')

    # Check if the user exists
    if clientes_exists(cursor, utilizador, password):
        print('\n' * 2)
        print('Login realizado com sucesso!')
        print('Bem-vindo, {}! É bom vê-lo!'.format(utilizador.title()))
    else:
        print('Email ou senha inválidos. Encerrando o programa...')
        conn.close()
        exit()
else:
    adicionar_cliente()

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
        Menu_Clientes()
    elif opcao == '2':
        print('Opção de veículos escolhida')
    elif opcao == '3':
        menu_faturas() 
    elif opcao == '4':
        print('')
    else:
        print('Opção inválida. Tente novamente.')

conn.close()
