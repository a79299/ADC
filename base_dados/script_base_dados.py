import sqlite3

conexao = sqlite3.connect('./database.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    nif INTEGER PRIMARY KEY,
                    nome TEXT,
                    apelido TEXT,
                    telefone TEXT,
                    data_nascimento DATE,
                    email TEXT
                )''')

conexao.commit()
conexao.close()

print("Base de dados criada com sucesso!")