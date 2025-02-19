from flask_restful import Resource, reqparse
from Models.user import Usuario

class UsuarioResource(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required = True, help= "Necessario que seja inserido um nome de usuário")
    arguments.add_argument('email', type=str, required=True, help= "Necessario que seja inserido um email")
    arguments.add_argument('password', type=str, required=True, help="Necessario que seja inserida uma senha")


    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self, id_usuario):
        pass


