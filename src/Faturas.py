import sqlite3

conexao = sqlite3.connect('../database.db')
cursor = conexao.cursor()

def criar_fatura(nif_cliente, matricula, descricao_servico, valor):

    """
    Cria uma nova fatura para um cliente e veículo específicos.

    :param nif_cliente: NIF do cliente
    :type nif_cliente: str
    :param matricula: Matrícula do veículo
    :type matricula: str
    :param descricao_servico: Descrição do serviço
    :type descricao_servico: str
    :param valor: Valor da fatura
    :type valor: float
    """
    
    conexao = sqlite3.connect('../database.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE nif=?", (nif_cliente,))
    cliente = cursor.fetchone()

    if cliente is None:
        print("Cliente não encontrado. Verifique o NIF.")
        conexao.close()
        return
    
    cursor.execute("SELECT * FROM veiculos WHERE matricula=?", (matricula,))
    veiculo = cursor.fetchone()

    if veiculo is None:
        print("Veículo não encontrado. Verifique a matrícula.")
        conexao.close()
        return

    cursor.execute("INSERT INTO faturas (nif_cliente, nome_cliente, apelido_cliente, telefone_cliente, matricula, marca, modelo, descricao_servico, valor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (cliente[0], cliente[1], cliente[2], cliente[3], veiculo[5], veiculo[1], veiculo[2], descricao_servico, valor))

    conexao.commit()

    print("Fatura criada com sucesso!")

def visualizar_faturas():
    conexao = sqlite3.connect('../database.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM faturas")
    faturas = cursor.fetchall()

    if not faturas:
        print("\nNão há faturas registradas.")
    else:
        print("\n======= Faturas =======")
        for fatura in faturas:
            print("Número da Fatura: {}".format(fatura[0]))
            print("NIF do Cliente: {}".format(fatura[1]))
            print("Nome do Cliente: {}".format(fatura[2]))
            print("Apelido do Cliente: {}".format(fatura[3]))
            print("Telefone do Cliente: {}".format(fatura[4]))
            print("Matrícula: {}".format(fatura[5]))
            print("Modelo do Veículo: {}".format(fatura[6]))
            print("Descrição do Serviço: {}".format(fatura[8]))
            print("Valor: {}€\n".format(fatura[9]))

    conexao.close()

def editar_fatura(numero_fatura):
    conexao = sqlite3.connect('../database.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM faturas WHERE numero_fatura=?", (numero_fatura,))
    fatura = cursor.fetchone()

    if fatura is None:
        print("\nFatura não encontrada. Verifique o número da fatura.")
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

    novo_telefone = input("\nDigite o novo telefone do cliente (ou pressione Enter para manter o atual): ").strip() or fatura[4]
    nova_matricula = input("Digite a nova matrícula do veículo (ou pressione Enter para manter a atual): ").strip() or fatura[5]
    nova_descricao_servico = input("Digite a nova descrição do serviço (ou pressione Enter para manter a atual): ").strip() or fatura[7]
    novo_valor_input = input("Digite o novo valor (ou pressione Enter para manter o atual): ")
    novo_valor = float(novo_valor_input) if novo_valor_input.strip() else fatura[8]

    cursor.execute("UPDATE faturas SET telefone_cliente=?, matricula=?, descricao_servico=?, valor=? WHERE numero_fatura=?", 
                   (novo_telefone, nova_matricula, nova_descricao_servico, novo_valor, numero_fatura))

    conexao.commit()
    conexao.close()

    print("\nFatura editada com sucesso!")

def eliminar_fatura(numero_fatura):
    conexao = sqlite3.connect('../database.db')
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

conexao.close()

def menu_faturas():
    while True:
        print("\n###############################")
        print("#        MENU DE FATURAS       #")
        print("###############################\n")
        print("Escolha uma opção:")
        print("1 - Criar Fatura")
        print("2 - Visualizar Faturas")
        print("3 - Editar Fatura")
        print("4 - Eliminar Fatura")
        print("0 - Voltar ao Menu Principal")

        opcao_fatura = input('Digite sua opção: ')

        if opcao_fatura == '0':
            break
        elif opcao_fatura == '1':
            nif_cliente = input("Digite o NIF do Cliente: ")
            matricula = input("Digite a Matrícula do Veículo: ")
            descricao_servico = input("Digite a Descrição do Serviço: ")
            valor = float(input("Digite o Valor: "))
            criar_fatura(nif_cliente, matricula, descricao_servico, valor)
        elif opcao_fatura == '2':
            visualizar_faturas()
        elif opcao_fatura == '3':
            numero_fatura_para_editar = input("Digite o número da fatura que deseja editar: ")
            editar_fatura(numero_fatura_para_editar)
        elif opcao_fatura == '4':
            numero_fatura = input("Digite o número da fatura que deseja eliminar: ")
            eliminar_fatura(numero_fatura)
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    menu_faturas()
