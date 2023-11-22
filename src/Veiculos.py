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