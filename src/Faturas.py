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

def visualizar_faturas():

    conexao = sqlite3.connect('./database.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM faturas")
    faturas = cursor.fetchall()

    if not faturas:
        print("Não há faturas registradas.")
    else:
        for fatura in faturas:
            print("Número da Fatura: {}".format(fatura[0]))
            print("NIF do Cliente: {}".format(fatura[1]))
            print("Nome do Cliente: {}".format(fatura[2]))
            print("Apelido do Cliente: {}".format(fatura[3]))
            print("Telefone do Cliente: {}".format(fatura[4]))
            print("Matrícula: {}".format(fatura[5]))
            print("Modelo do Veículo: {}".format(fatura[6]))
            print("Descrição do Serviço: {}".format(fatura[8]))
            print("Valor: {}\n".format(fatura[9]))

    conexao.close()

visualizar_faturas()

def editar_fatura():
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()

    numero_fatura = input("Digite o número da fatura que deseja editar: ")

    cursor.execute("SELECT * FROM faturas WHERE numero_fatura=?", (numero_fatura,))
    fatura = cursor.fetchone()

    if fatura is None:
        print("Fatura não encontrada. Verifique o número da fatura.")
        conexao.close()
        return
    
    print("\nInformações atuais da fatura:")
    print("Número da Fatura:", fatura[0])
    print("NIF do Cliente:", fatura[1])
    print("Nome do Cliente:", fatura[2])
    print("Apelido do Cliente:", fatura[3])
    print("Telefone do Cliente:", fatura[4])
    print("Matrícula:", fatura[5])
    print("Modelo do Veículo:", fatura[6])
    print("Descrição do Serviço:", fatura[7])
    print("Valor:", fatura[8])

    novo_telefone = input("\nDigite o novo telefone do cliente (ou pressione Enter para manter o atual): ").strip()
    nova_matricula = input("Digite a nova matrícula do veículo (ou pressione Enter para manter a atual): ").strip()
    nova_descricao_servico = input("Digite a nova descrição do serviço (ou pressione Enter para manter a atual): ").strip()
    novo_valor = float(input("Digite o novo valor (ou pressione Enter para manter o atual): ")) 

    cursor.execute("UPDATE faturas SET telefone_cliente=?, matricula=?, descricao_servico=?, valor=? WHERE numero_fatura=?", 
                   (novo_telefone, nova_matricula, nova_descricao_servico, novo_valor, numero_fatura))

    conexao.commit()
    conexao.close()

    print("\nFatura editada com sucesso!")

editar_fatura()

def eliminar_fatura(numero_fatura):

    conexao = sqlite3.connect('./database.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM faturas WHERE numero_fatura=?", (numero_fatura,))
    fatura = cursor.fetchone()

    if fatura is None:
        print("Fatura não encontrada.")
    else:
        cursor.execute("DELETE FROM faturas WHERE numero_fatura=?", (numero_fatura,))
        print("Fatura removida com sucesso.")

    conexao.commit()
    conexao.close()

eliminar_fatura(1)

conexao.close()