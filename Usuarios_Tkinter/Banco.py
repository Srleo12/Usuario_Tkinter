import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db') # Cria/abre o arquivo do banco de dados
        self.createTable()
        
    def createTable(self):
        c = self.conexao.cursor() # Cria um cursor para executar comandos SQL
        c.execute("""create table if not exists usuarios (
                  idusuario integer primary key autoincrement ,
                  nome text,
                  telefone text,
                  email text,
                  usuario text,
                  senha text)""") # Cria a tabela se ela não existir
        
        self.conexao.commit()
        c.close()
