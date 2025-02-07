from flask_restful import Resource, reqparse
from Resource import task
import sqlite3

class Task(Resource):

    #utilizando para manter a consistencia de entrada de variaveis
    arguments = reqparse.RequestParser()
    arguments.add_argument('title', type=str, required= True, help= "O campo title não pode ser deixado em branco.")
    arguments.add_argument('description', type=str, required= True, help= "O campo description não pode ser deixado em branco")

    def get(self, id_task):
        task = Models.Task.find_task(id_task)

        if task:
            return task.json()
        return {'message': 'task not found'}, 404

    def post(self, id_task):
        if Models.Task.find_task(id_task):
            return {f"message": f"task id {id_task} already exixts"}


        dados = Task.arguments.parse_args()
        task = Task(id_task, **dados)
        try:
            save_task()
        except:
            return {'message': "an internal error occured trying save task"}, 500
        return task.json()
    

