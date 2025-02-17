from extensions import banco
#aqui eu crio o modelo de task
#serão necerrios ID, titulo e descrição

class Task(banco.Model):
    __tablename__ = "tarefas"

    id_task = banco.Column(banco.Integer, primary_key=True)
    title = banco.Column(banco.String(50))
    description = banco.Column(banco.String(500))

    #______________________________________________________


    def __init__(self, title, description):

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

    def delete_task(self, id_task):
        banco.session.delete(id_task)
        banco.session.commit()

    @classmethod
    def find_task(cls, id_task):
        task = cls.query.filter_by(id_task=id_task).first()
        if task:
            return task
        return None


