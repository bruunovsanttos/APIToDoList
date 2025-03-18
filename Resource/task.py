from flask_restful import Resource, reqparse
from Models.task import Task
from flask_jwt_extended import jwt_required, get_jwt_identity



class TaskResource(Resource):

    #utilizando para manter a consistencia de entrada de variaveis
    arguments = reqparse.RequestParser()
    arguments.add_argument('title', type=str, required= True, help= "O campo title não pode ser deixado em branco.")
    arguments.add_argument('description', type=str, required= True, help= "O campo description não pode ser deixado em branco")

    @jwt_required()
    def get(self, id_task=None):
        id_user = get_jwt_identity() #obtem o id do usuario

        if id_task:
            task = Task.find_task(int(id_task))
            if task and task.id_user == int(id_user): #verifica de qual usuario é e como estava recebendo string não funcionanva
                return task.json(), 200
            return {'message': 'Tarefa não encontrada ou não pertence a este usuário'}, 404
        else:
            tasks = Task.find_task_by_user(id_user) #chama todas as tasks do usuario

            if not tasks:
                return {'message': "Any tasks for this user"}, 404

            task_list = [] #lista para adicionar cada task encontrada.

            for task in tasks: #se tem uma task em tasks
                task_list.append(task.json()) #adiciona no task_list
            return task_list, 200 #mostra a lista e retorna a requisição

    @jwt_required()
    def post(self):
        id_user = get_jwt_identity()
        dados = self.arguments.parse_args()
        task = Task(title=dados['title'],description=dados['description'], id_user=id_user)

        try:
            task.save_task()
            return task.json(), 201
        except:
            return {'message': "an internal error occured trying save task"}, 500
    @jwt_required()
    def put(self, id_task):
        dados = TaskResource.arguments.parse_args()

        task = Task.find_task(id_task)

        if task:

            if task.id_user != get_jwt_identity():
                return {'message': "Você não tem permissão para atualizar essa tarefa"}, 403

            task.update_task(**dados)
            task.save_task()
            return task.json(), 200
        task = Task(**dados)
        try:
            task.save_task(), 200
        except:
            {'message': 'An internal error occurred trying save task'}, 500

        return task.json(), 201


    @jwt_required()
    def delete(self, id_task):
        task = Task.find_task(id_task)

        if task:
            Task.delete_task(id_task)
            return {'message': f"task {id_task} deleted succeful"}, 204
        return{'message': f"An internal error occured and task is not deleted"}

