import sqlite3
from tabulate import tabulate

def listar_todos_veiculos():
    conexao = sqlite3.connect('../database.db')
    cursor = conexao.cursor()


    query_select_veiculos = '''SELECT v.id_veiculo, v.marca || ' ' || v.modelo AS veiculo,
                               v.matricula, v.ano, v.cor, c.nome || ' ' || c.apelido AS proprietario
                               FROM veiculos v
                               JOIN clientes c ON v.nif = c.nif'''


    cursor.execute(query_select_veiculos)


    resultados = cursor.fetchall()

    dados_tabela = []
    cabecalho = ["Id Veiculo", "Veiculo", "Matricula", "Ano", "Cor", "Proprietario"]
    for veiculo in resultados:
        dados_tabela.append(list(veiculo))

    print("_" * 100)
    print(" " * 36 + "Lista de veiculos")
    print("_" * 100)
    print(tabulate(dados_tabela, headers=cabecalho, tablefmt="pipe"))

    conexao.close()


def listar_carros_cliente(nif_cliente):
    conexao = sqlite3.connect('../database.db')
    cursor = conexao.cursor()

    query_dados_cliente = '''SELECT c.nome, v.id_veiculo, v.marca, v.modelo, v.matricula, v.ano, v.cor
                                 FROM clientes c
                                 INNER JOIN veiculos v ON c.nif = v.nif
                                 WHERE c.nif = ?'''

    cursor.execute(query_dados_cliente, (nif_cliente,))
    dados_cliente_veiculos = cursor.fetchall()

    if dados_cliente_veiculos:
        cabecalho = ["Id Veiculo", "Marca", "Modelo", "Matricula", "Ano", "Cor"]

        nome_cliente = dados_cliente_veiculos[0][0]
        veiculos_cliente = [veiculo[1:] for veiculo in dados_cliente_veiculos]

        print(f"Carros do cliente {nome_cliente} com NIF {nif_cliente}:\n")
        print(tabulate(veiculos_cliente, headers=cabecalho, tablefmt="pretty"))

    else:
        print(f"O cliente com NIF {nif_cliente} não possui carros.")

    conexao.close()


def adicionar_veiculo(nif_cliente, marca, modelo, matricula, ano, cor):
    conexao = sqlite3.connect('../database.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE nif = ?", (nif_cliente,))
    cliente_existente = cursor.fetchone()

    if cliente_existente:
        cursor.execute('''INSERT INTO veiculos (marca, modelo, matricula, ano, cor, nif)
                          VALUES (?, ?, ?, ?, ?, ?)''', (marca, modelo, matricula, ano, cor, nif_cliente))
        conexao.commit()

        print("Veículo adicionado com sucesso!")

    else:
        print("O cliente não existe na base de dados. Não foi possível adicionar o veículo.")

    conexao.close()


def eliminar_veiculo(matricula):
    conexao = sqlite3.connect('../database.db')
    cursor = conexao.cursor()

    query_verificar = '''SELECT * FROM veiculos WHERE matricula = ?'''
    cursor.execute(query_verificar, (matricula,))
    veiculo = cursor.fetchone()

    if veiculo:
        query_eliminar = '''DELETE FROM veiculos WHERE matricula = ?'''
        cursor.execute(query_eliminar, (matricula,))
        conexao.commit()
        print(f"Veículo com a matrícula '{matricula}' foi eliminado com sucesso.")
    else:
        print(f"Veículo com a matrícula '{matricula}' não encontrado.")

    conexao.close()

def menu_veiculos():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Listar todos os veículos")
        print("2. Listar carros de um cliente")
        print("3. Adicionar veículo")
        print("4. Eliminar veículo")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_todos_veiculos()
        elif opcao == '2':
            nif = input("Digite o NIF do cliente: ")
            listar_carros_cliente(nif)
        elif opcao == '3':
            nif = input("Digite o NIF do cliente: ")
            marca = input("Marca do veículo: ")
            modelo = input("Modelo do veículo: ")
            matricula = input("Matrícula do veículo: ")
            ano = input("Ano do veículo: ")
            cor = input("Cor do veículo: ")
            adicionar_veiculo(nif, marca, modelo, matricula, ano, cor)
        elif opcao == '4':
            matricula = input("Digite a matrícula do veículo a eliminar: ")
            eliminar_veiculo(matricula)
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_veiculos()