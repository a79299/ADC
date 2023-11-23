import sqlite3

def conectar_banco_dados():
    """
    Conexão a base de dados

    :return: Retorna uma conexão com a Base de dados SQLite.

    :rtype: sqlite3.Connection
    """
    return sqlite3.connect('database.db')

def fechar_conexao(conexao, cursor=None):
    """
    Fecha conexão base de dados

    :param conexao: Conexão com a Base de dados.

    :type conexao: sqlite3.Connection

    :param cursor: Cursor para executar consultas na Base de dados, defaults to None.

    :type cursor: sqlite3.Cursor, optional
    """
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()

def adicionar_cliente():
    """
    Solicita informações do utilizador para adicionar um novo cliente a Base de dados.
    
    :raises sqlite3.Error: Se ocorrer um erro durante a execução da consulta SQL.
    """
    nome = input("Digite o seu nome: ")
    apelido = input("Digite o seu apelido: ")
    telefone = input("Digite o seu telefone: ")
    data_nascimento = input("Digite a sua data de nascimento: ")
    nif = input("Digite o seu nif: ")
    email = input("Digite o seu e-mail: ")

    try:
        conexao = conectar_banco_dados()
        cursor = conexao.cursor()

        consulta = "INSERT INTO clientes (nome, apelido, telefone, data_nascimento, nif, email) VALUES (?, ?, ?, ?, ?, ?)"
        valores = (nome, apelido, telefone, data_nascimento, nif, email)
        cursor.execute(consulta, valores)
        conexao.commit()

        print(f"Cliente {nome} ({apelido}) adicionado com sucesso!")

    except sqlite3.Error as erro:
        print(f"Erro ao adicionar o cliente: {erro}")

    finally:
        fechar_conexao(conexao, cursor)

def obter_cliente(nif):
    """
    
    Obtém as informações de um cliente com base no NIF

    :param nif: NIF do cliente

    :type nif: str

    :return: As informações do cliente

    :rtype: tuple or None

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da consulta SQL
    """
    try:
        conexao = conectar_banco_dados()
        cursor = conexao.cursor()

        consulta = "SELECT * FROM clientes WHERE nif = ?"
        cursor.execute(consulta, (nif,))
        cliente = cursor.fetchone()

        return cliente

    except sqlite3.Error as erro:
        print(f"Erro ao obter cliente: {erro}")

    finally:
        fechar_conexao(conexao, cursor)

def visualizar_cliente(nif):
    """
    Visualiza as informações de um cliente com base no NIF

    :param nif: NIF do cliente

    :type nif: str
    """
    cliente = obter_cliente(nif)

    if not cliente:
        print(f"Nenhum cliente encontrado com NIF {nif}.")
    else:
        print("\nInformações do Cliente:")
        print("\n")
        print(f"Nome: {cliente[1]}")
        print(f"Apelido: {cliente[2]}")
        print(f"Telefone: {cliente[3]}")
        print(f"Data de Nascimento: {cliente[4]}")
        print(f"NIF: {cliente[0]}")
        print(f"E-mail: {cliente[5]}")

def atualizar_cliente(nif):
    """
    Atualiza as informações de um cliente com base no NIF

    :param nif: NIF do cliente

    :type nif: str

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da consulta SQL
    """
    cliente = obter_cliente(nif)

    if not cliente:
        print(f"Nenhum cliente encontrado com NIF {nif}.")
        return

    try:
        print("\nInformações do Cliente antes da atualização:")
        print("\n")
        print(f"Nome: {cliente[1]}")
        print(f"Apelido: {cliente[2]}")
        print(f"Telefone: {cliente[3]}")
        print(f"Data de Nascimento: {cliente[4]}")
        print(f"NIF: {cliente[0]}")
        print(f"E-mail: {cliente[5]}")

        novo_nome = input("Digite o novo nome: ")
        novo_apelido = input("Digite o novo apelido: ")
        novo_telefone = input("Digite o novo telefone: ")
        novo_data_nascimento = input("Digite a nova data de nascimento: ")
        novo_email = input("Digite o novo e-mail: ")

        with conectar_banco_dados() as conexao:
            cursor = conexao.cursor()
            consulta = "UPDATE clientes SET nome=?, apelido=?, telefone=?, data_nascimento=?, email=? WHERE nif=?"
            valores = (novo_nome, novo_apelido, novo_telefone, novo_data_nascimento, novo_email, nif)
            cursor.execute(consulta, valores)
            conexao.commit()

        print(f"Informações do cliente com NIF {nif} atualizadas com sucesso.")

    except sqlite3.Error as erro:
        print(f"Erro ao atualizar cliente: {erro}")

    finally:
        fechar_conexao(conexao, cursor)

def eliminar_cliente(nif):
    """
    Exclui um cliente com base no NIF

    :param nif: NIF do cliente a ser excluído

    :type nif: str

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da consulta SQL
    """
    cliente = obter_cliente(nif)

    if not cliente:
        print(f"Nenhum cliente encontrado com NIF {nif}.")
        return

    try:
        visualizar_cliente(nif)

        confirmacao = input(f"Tem certeza que deseja excluir o cliente com NIF {nif}? (s/n): ")
        if confirmacao.lower() == 's':
            with conectar_banco_dados() as conexao:
                cursor = conexao.cursor()
                consulta = "DELETE FROM clientes WHERE nif = ?"
                cursor.execute(consulta, (nif,))
                conexao.commit()

            print(f"Cliente com NIF {nif} excluído com sucesso.")
        else:
            print("Exclusão cancelada.")

    except sqlite3.Error as erro:
        print(f"Erro ao excluir cliente: {erro}")

    finally:
        fechar_conexao(conexao, cursor)

def visualizar_cliente_menu():
    """
    Solicita o NIF do cliente e exibe suas informações

    :raises sqlite3.Error: Se ocorrer um erro durante a execução da consulta SQL
    """
    try:
        nif_cliente = input("Digite o seu NIF: ")
        conexao = conectar_banco_dados()
        cursor = conexao.cursor()

        consulta = "SELECT * FROM clientes WHERE nif = ?"
        cursor.execute(consulta, (nif_cliente,))
        cliente = cursor.fetchone()

        if not cliente:
            print(f"Nenhum cliente encontrado com NIF {nif_cliente}.")
        else:
            print("\nInformações do Cliente:")
            print(f"Nome: {cliente[1]}")
            print(f"Apelido: {cliente[2]}")
            print(f"Telefone: {cliente[3]}")
            print(f"Data de Nascimento: {cliente[4]}")
            print(f"NIF: {cliente[0]}")
            print(f"E-mail: {cliente[5]}")

    except sqlite3.Error as erro:
        print(f"Erro ao visualizar cliente: {erro}")

    finally:
        fechar_conexao(conexao, cursor)

def Menu_Clientes():
    """
    Exibe um menu interativo para gerir os clientes.
    """
    while True:
        print("\n===================================")
        print("=          MENU PRINCIPAL         =")
        print("===================================\n")
        print("Escolha uma opção:")
        print("1 - Adicionar Cliente")
        print("2 - Visualizar Cliente")
        print("3 - Editar Cliente")
        print("4 - Eliminar Cliente")
        print("0 - SAIR")
        opcao = input('Digite sua opção: ')

        if opcao == '0':
            print('Até breve!')
            print('Fechando o programa...')
            break
        elif opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            nif_cliente = input("Digite o NIF do cliente que deseja visualizar: ")
            visualizar_cliente(nif_cliente)
        elif opcao == '3':
            nif_cliente = input("Digite o NIF do cliente que deseja atualizar: ")
            atualizar_cliente(nif_cliente)
        elif opcao == '4':
            nif_cliente = input("Digite o NIF do cliente que deseja eliminar: ")
            eliminar_cliente(nif_cliente)
        else:
            print("Opção inválida. Tente novamente.")
