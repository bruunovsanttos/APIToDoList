from sqlalchemy import banco
#aqui eu crio o modelo de task
#serão necerrios ID, titulo e descrição

class Task(): #importar banco de dados
    #colocar como deve ser estruturado o banco de dados
    __tablename__ = "tarefas"

    id_task = banco.Collumn(banco.Integer, primary_key=True)
    title = banco.Collumn(banco.String(50))
    description = banco.Collumn(banco.String(500))

    #______________________________________________________


    def __init__(self, id_task, title, description):
        self.id_task = id_task
        self.title = title
        self.description = description

    def json(self):
        return{
            'id_task': self.id_task,
            'title': self.title,
            'description': self.description
        }

    def save_task(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_task(self):
        banco.session.delete()
        banco.session.commit()

    @classmethod
    def find_task(cls, id_task):
        task = cls.query.filter_by(id_task=id_task).first()
        if task:
            return task
        return None


