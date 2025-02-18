from flask_restful import Resource, reqparse
from Models.task import Task
import sqlite3

class TaskResource(Resource):

    #utilizando para manter a consistencia de entrada de variaveis
    arguments = reqparse.RequestParser()
    arguments.add_argument('title', type=str, required= True, help= "O campo title não pode ser deixado em branco.")
    arguments.add_argument('description', type=str, required= True, help= "O campo description não pode ser deixado em branco")

    def get(self, id_task=None):
        if id_task:
            task = Task.find_task(id_task)
            if task:
                return task.json(), 200
            return {'message': 'task not found'}, 404
        else:
            tasks = Task.query.all() #chama todas as tasks do banco de dados
            task_list = [] #lista para adicionar cada task encontrada.

            for task in tasks: #se tem uma task em task
                task_list.append(task.json()) #adiciona no task_list
            return task_list, 200 #mostra a lista e retorna a requisição


    def post(self):

        dados = self.arguments.parse_args()
        task = Task(**dados)

        try:
            task.save_task()
            return task.json(), 201
        except:
            return {'message': "an internal error occured trying save task"}, 500

    def put(self, id_task):
        dados = TaskResource.arguments.parse_args()

        task = Task.find_task(id_task)

        if task:
            task.update_task(**dados)
            task.save_task()
            return task.json(), 200
        task = Task(**dados) #remover id task pois é gerado automaticamente pelo banco. 
        try:
            task.save_task(), 200
        except:
            {'message': 'An internal error occu rred trying save post'}, 500

        return task.json(), 201



    def delete(self, id_task):
        task = Task.find_task(id_task)

        if task:
            Task.delete_task(id_task)
            return {'message': f"task {id_task} deleted succeful"}, 200
        return{'message': f"An internal error occured and task is not deleted"}

