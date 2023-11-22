import sqlite3

conexao = sqlite3.connect('./database.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    nif INTEGER PRIMARY KEY,
                    nome TEXT,
                    apelido TEXT,
                    telefone TEXT,
                    data_nascimento DATE,
                    email TEXT,
                    password TEXT
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

cursor.execute('''CREATE TABLE IF NOT EXISTS faturas (
                    numero_fatura INTEGER PRIMARY KEY,
                    nif_cliente INTEGER,
                    nome_cliente TEXT,
                    apelido_cliente TEXT,
                    telefone_cliente TEXT,
                    matricula TEXT,
                    marca TEXT,
                    modelo TEXT,
                    descricao_servico TEXT,
                    valor DECIMAL,
                    FOREIGN KEY (nif_cliente) REFERENCES clientes(nif),
                    FOREIGN KEY (matricula, marca, modelo) REFERENCES veiculos(matricula, marca, modelo)
                )''')

conexao.commit()
conexao.close()

print("Base de dados criada com sucesso!")