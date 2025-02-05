#modelo de usuario.
#usuario necessita de nome, email, senha

class Usuario(): #colocar o banco de dados para receber aqui
    def __init__(self, name, email password):
        self.name = name
        self.email = email
        self.password = password

    def json(self):
        return{
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

