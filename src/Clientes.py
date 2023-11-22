def conectar_banco_dados():
    return sqlite3.connect('database.db')

def fechar_conexao(conexao, cursor=None):

    if cursor:
        cursor.close()
    if conexao:
        conexao.close()

def adicionar_cliente():
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