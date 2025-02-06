from sqlalchemy import banco
#modelo de usuario.
#usuario necessita de nome, email, senha

class Usuario(): #colocar o banco de dados para receber aqui
    # aqui vai ficar o modelo de banco de dados do usuario
    __tablename__ = "user"

    id_user = banco.Collumn(banco.Integer, primary_key=True)
    name = banco.Collumn(banco.String(60))
    email = banco.Collumn(banco.String(60))
    password = banco.Collumn(banco.String(20))

    #_____________________________________________________
    def __init__(self, id_usuario, name, email, password):
        self.id_user = id_usuario
        self.name = name
        self.email = email
        self.password = password

    def json(self):
        return{
            'id_usuario': self.id_user,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
    @classmethod
    def find_user(cls, id_user):
        user = cls.query.filter_by(id_user=id_user).first

        if user:
            return user
        return None

    
