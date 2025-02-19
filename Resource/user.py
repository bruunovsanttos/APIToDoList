from flask_restful import Resource, reqparse
from Models.user import Usuario


class UsuarioResource(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required = True, help= "Necessario que seja inserido um nome de usuário")
    arguments.add_argument('email', type=str, required=True, help= "Necessario que seja inserido um email")
    arguments.add_argument('password', type=str, required=True, help="Necessario que seja inserida uma senha")


    def get(self):
        if id_usuario:
            user = Usuario.find_user(id_usuario)
            if user:
                return user.json(), 200
            return {'message':'user not found'}
        else:
            users = Usuario.query.all()
            user_list = []
            for user in users:
                user_list.append(user.json())
            return user_list, 200
        return {'message':'user not found'}

    def post(self):
        pass

    def put(self):
        pass

    def delete(self, id_usuario):
        pass


