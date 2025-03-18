from extensions import banco
import bcrypt
#usuario necessita de nome, email, senha

class Usuario(banco.Model): #colocar o banco de dados para receber aqui
    # aqui vai ficar o modelo de banco de dados do usuario
    __tablename__ = "user"

    id_user = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(60))
    email = banco.Column(banco.String(60), unique=True) #unique gera apenas um usuario com o mesmo email
    password = banco.Column(banco.String(200))#tamanho grande para utilizar o hash sem quebrar

    #_____________________________________________________
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = self.hash_password(password)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'),salt).decode("utf-8")

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def json(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
    @classmethod
    def find_user(cls, id_user):
        user = cls.query.filter_by(id_user=id_user).first()

        if user:
            return user
        return None

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    @classmethod
    def delete_user(cls, id_user):
        user = cls.find_user(id_user)

        if user:
            banco.session.delete(user)
            banco.session.commit()

    def update_user(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
