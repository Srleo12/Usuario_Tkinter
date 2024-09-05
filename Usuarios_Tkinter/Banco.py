import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')  # Cria/abre o arquivo do banco de dados
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()  # Cria um cursor para executar comandos SQL
        c.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                      idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                      nome TEXT,
                      telefone TEXT,
                      email TEXT,
                      usuario TEXT,
                      senha TEXT)""")  # Cria a tabela se ela não existir
        self.conexao.commit()
        c.close()
