from flask_restful import Resource, reqparse
from Models.user import Usuario
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from blacklist import BLACKLIST


class UsuarioResource(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required = True, help= "Necessario que seja inserido um nome de usuário")
    arguments.add_argument('email', type=str, required=True, help= "Necessario que seja inserido um email")
    arguments.add_argument('password', type=str, required=True, help="Necessario que seja inserida uma senha")


    def get(self, id_user=None):
        if id_user:
            user = Usuario.find_user(id_user)
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
        dados = self.arguments.parse_args()
        user = Usuario(**dados)

        try:
            user.save_user()
            return user.json(), 201
        except:
            return {'message': "an internal error occured trying save task"}, 500

    def put(self, id_user):
        dados = UsuarioResource.arguments.parse_args()

        user = Usuario.find_user(id_user)

        if user:
            user.update_user(**dados)
            user.save_user()
            return user.json(), 200
        user = Usuario(**dados)
        try:
            user.save_user(), 200
        except:
            {'message':'An internal error occured trying save user'}, 500

        return user.json(), 201

    def delete(self, id_user):

        user = Usuario.find_user(id_user)

        if user:
            Usuario.delete_user(id_user)
            return{'message':f'{user} deleted succeful'}, 200
        return{'message': f"An internal error occured and user is not deleted"}


class UserLogin(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('email', type=str, required=True, help="Email é obrigatório")
    arguments.add_argument('password', type=str, required=True, help="Senha é obrigatório")


    def post(self):
        dados = self.arguments.parse_args()
        user = Usuario.query.filter_by(email=dados['email']).first()

        #nesse ponto verificar como fazer um hash depois de terminar o codigo

        if user and user.password == dados['password']:
            access_token = create_access_token(identity=user.id_user) #identity=user.id_user armazena a identidade do usuário dentro do token, normalmente o ID do usuário.
            return {'token':access_token}, 200

        return {'message': f'Credenciais de usuario do usuário {user.id_user} incorretas'}, 401






