from extensions import banco
#aqui eu crio o modelo de task
#serão necerrios ID, titulo e descrição

class Task(banco.Model):
    __tablename__ = "tarefas"

    id_task = banco.Column(banco.Integer, primary_key=True)
    title = banco.Column(banco.String(50))
    description = banco.Column(banco.String(500))
    id_user = banco.Column(banco.Integer, banco.ForeignKey('user.id_user'), nullable=False) #chave estrangeira para vincular ao usuario

    #______________________________________________________


    def __init__(self, title, description, id_user):

        self.title = title
        self.description = description
        self.id_user = id_user


    def json(self):
        return{
            'id_task': self.id_task,
            'title': self.title,
            'description': self.description
            'id_user': self.id_user
        }

    def save_task(self):
        banco.session.add(self)
        banco.session.commit()

    def update_task(self, title, description):
        self.title = title
        self.description = description

    @classmethod
    def delete_task(cls, id_task):
        task = cls.find_task(id_task)
        if task:
            banco.session.delete(task)
            banco.session.commit()

    @classmethod
    def find_task(cls, id_task):
        task = cls.query.filter_by(id_task=id_task).first()
        if task:
            return task
        return None

    @classmethod
    def find_task_by_user(cls, id_user):
        return cls.query.filter_by(id_user=id_user).all() #chama todas tasks por usuario
    


