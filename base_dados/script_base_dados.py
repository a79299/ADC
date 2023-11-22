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

cursor.execute('''CREATE TABLE IF NOT EXISTS veiculos (
                    id_veiculo INTEGER PRIMARY KEY,
                    marca TEXT,
                    modelo TEXT,
                    cor TEXT,
                    ano DATE,
                    matricula TEXT,
                    nif INTEGER,
                    FOREIGN KEY (nif) REFERENCES clientes(nif)
                )''')

conexao.commit()
conexao.close()

print("Base de dados criada com sucesso!")