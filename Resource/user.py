from flask_restful import Resource, reqparse
from Models.user import Usuario
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from blacklist import BLACKLIST


class UsuarioResource(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('name', type=str, required = True, help= "Necessario que seja inserido um nome de usuário")
    arguments.add_argument('email', type=str, required=True, help= "Necessario que seja inserido um email")
    arguments.add_argument('password', type=str, required=True, help="Necessario que seja inserida uma senha")

    @jwt_required()
    def get(self, id_user=None):
        if id_user:
            user = Usuario.find_user(id_user)
            if user:
                return user.json(), 200
            return {'message':'user not found'}, 404
        else:
            users = Usuario.query.all()
            user_list = []
            for user in users:
                user_list.append(user.json())
            return user_list, 200
        return {'message':'user not found'}

    @jwt_required()
    def post(self):
        dados = self.arguments.parse_args()
        user = Usuario(name=dados['name'],email=dados['email'], password=dados['password'])#ajuda a fazer hash de senha melhor declarando de modo explicito

        try:
            user.save_user()
            return user.json(), 201
        except:
            return {'message': "an internal error occured trying save user"}, 500

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
    @jwt_required()
    def delete(self, id_user):

        user = Usuario.find_user(id_user)

        if user:
            Usuario.delete_user(id_user)
            return{'message':f'{user} deleted succeful'}, 200
        return{'message': f"An internal error occured and user is not deleted"}, 400


class UserLogin(Resource):

    arguments = reqparse.RequestParser()
    arguments.add_argument('email', type=str, required=True, help="Email é obrigatório")
    arguments.add_argument('password', type=str, required=True, help="Senha é obrigatório")


    def post(self):
        dados = self.arguments.parse_args()
        user = Usuario.query.filter_by(email=dados['email']).first()

        if user and user.check_password(dados['password']):#aqui ja esta comparando o hash da senha com a senha
            access_token = create_access_token(identity=str (user.id_user)) #identity=user.id_user armazena a identidade do usuário dentro do token, normalmente o ID do usuário.
                #------------------------------------------------
                # Verificar como criar um token temporario tambem
                #------------------------------------------------
            return {'token':access_token}, 200

        return {'message': f'Credenciais de usuario do usuário incorretas'}, 401

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLACKLIST.add(jti)
        return {"message":"Successfully logget out"}, 200




