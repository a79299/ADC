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