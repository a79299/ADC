import sqlite3

conexao = sqlite3.connect('./database.db')
cursor = conexao.cursor()


clientes = [
    (123456789, 'João', 'Silva', '123456789', '1990-01-01', 'joao@email.com', 'abc'),
    (987654321, 'Maria', 'Souza', '987654321', '1985-05-15', 'maria@email.com', '123'),
    (111222333, 'Carlos', 'Ribeiro', '111222333', '1988-09-30', 'carlos@email.com', 'sporting'),
    (444555666, 'Ana', 'Oliveira', '444555666', '1995-03-12', 'ana@email.com', 'benfica'),
    (777888999, 'Pedro', 'Santos', '777888999', '1980-07-25', 'pedro@email.com', 'porto'),
]

cursor.executemany("INSERT INTO clientes (nif, nome, apelido, telefone, data_nascimento, email, password) VALUES (?, ?, ?, ?, ?, ?, ?)", clientes)


veiculos = [
    (1, 'Toyota', 'Corolla', 'Azul', '2020-01-01', 'AB123CD', 123456789),
    (2, 'Ford', 'Focus', 'Preto', '2018-05-20', 'XY987ZW', 987654321),
    (3, 'Honda', 'Civic', 'Vermelho', '2019-10-15', 'CD456EF', 111222333),
    (4, 'Chevrolet', 'Cruze', 'Branco', '2022-02-28', 'FG123HI', 444555666),
    (5, 'Volkswagen', 'Golf', 'Prata', '2017-08-10', 'JK789LM', 777888999),
]

cursor.executemany("INSERT INTO veiculos (id_veiculo, marca, modelo, cor, ano, matricula, nif) VALUES (?, ?, ?, ?, ?, ?, ?)", veiculos)

conexao.commit()
conexao.close()

print("Cinco clientes e Cinco veículos adicionados com sucesso!")