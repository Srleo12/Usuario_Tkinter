from Banco import Banco


class Usuarios(object):

    # Atributos que representam os campos do banco de dados
    def __init__(self, idusuario = 0, nome = "", telefone = "", email = "", usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):

        
        banco = Banco()
        try:

            # Comando SQL para inserir um novo usuário
            c = banco.conexao.cursor()
            c.execute("insert into usuarios (nome, telefone, email,usuario, senha) values ('" + self.nome + "', '" +
                      self.telefone + "', '" + self.email + "', '" +
                      self.usuario + "', '" + self.senha + "' )")
            
            # Confirma a inserção
            banco.conexao.commit()
            c.close()
            
            return "Usuário cadastrado com sucesso !"
        except:
            return "Ocorreu um erro na inserção do usuário"
    
    def updateUser(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            # Comando SQL para atualizar os dados de um usuário existente
            c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where idusuario = " + self.idusuario + " ")

            # Confirma a atualização
            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso !"
        except:
            return "Ocorreu um erro na alteração do usuário"
    
    
    def deleteUser(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()

            # Comando SQL para deletar um usuário com base no id
            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            # Confirma a exclusão
            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso !"
        except:
            return "Ocorreu um erro na exclusão do usuário"
    
    def selectUser(self, idusuario):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()

            # Comando SQL para selecionar um usuário com base no id
            c.execute("select * from usuarios where idusuario = " + idusuario + " ")
            
            # Preenche os atributos com os dados retornados do banco
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso !"
        except:
            return "Ocorreu um erro na busca do usuário"
