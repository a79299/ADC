import sqlite3

conexao = sqlite3.connect('./database.db')
cursor = conexao.cursor()

def criar_fatura():

    nif_cliente = input("Digite o NIF do Cliente: ")
    matricula = input("Digite a Matrícula do Veículo: ")
    descricao_servico = input("Digite a Descrição do Serviço: ")
    valor = float(input("Digite o Valor: ")) 

    cursor.execute("SELECT * FROM clientes WHERE nif=?", (nif_cliente,))
    cliente = cursor.fetchone()

    if cliente is None:
        print("Cliente não encontrado. Verifique o NIF.")
        return

    cursor.execute("SELECT * FROM veiculos WHERE matricula=?", (matricula,))
    veiculo = cursor.fetchone()

    if veiculo is None:
        print("Veículo não encontrado. Verifique a matrícula.")
        return

    cursor.execute("INSERT INTO faturas (nif_cliente, nome_cliente, apelido_cliente, telefone_cliente, matricula, marca, modelo, descricao_servico, valor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (cliente[0], cliente[1], cliente[2], cliente[3], veiculo[5], veiculo[1], veiculo[2], descricao_servico, valor))

    conexao.commit()

    print("Fatura criada com sucesso!")

criar_fatura()



conexao.close()