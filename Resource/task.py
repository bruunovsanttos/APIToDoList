from flask_restful import Resource, reqparse
from Models import Task, User
import sqlite3

class Task(Resource):

    #utilizando para manter a consistencia de entrada de variaveis
    arguments = reqparse.RequestParser()
    arguments.add_argument('title', type=str, required= True, help= "O campo title não pode ser deixado em branco.")
    arguments.add_argument('description', type=str, required= True, help= "O campo description não pode ser deixado em branco")

    def get(self, id_task):
        task = Task.find_task(id_task)

        if task:
            return task.json(), 200
        return {'message': 'task not found'}, 404

    def post(self):

        dados = self.arguments.parse_args()
        task = Task(**dados)

        try:
            task.save_task()
            return task.json(), 201
        except:
            return {'message': "an internal error occured trying save task"}, 500



