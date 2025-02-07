from flask_restful import Resource, reqparse
from Resource import task
import sqlite3

class Task(Resource):

    #utilizando para manter a consistencia de entrada de variaveis
    arguments = reqparse.RequestParser()
    arguments.add_argument('title', type=str, required= True, help= "O campo title não pode ser deixado em branco.")
    arguments.add_argument('description', type=str, required= True, help= "O campo description não pode ser deixado em branco")

    def get(self, id_task):
        task = Models.task.find_task(id_task)

        if task:
            return task.json()
        return {'message': 'task not found'}, 404
    
