#aqui eu crio o modelo de task
#serão necerrios ID, titulo e descrição

class Task(): #importar banco de dados
    #colocar como deve ser estruturado o banco de dados







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