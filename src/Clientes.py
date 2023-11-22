def conectar_banco_dados():
    return sqlite3.connect('database.db')

def fechar_conexao(conexao, cursor=None):
    
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()