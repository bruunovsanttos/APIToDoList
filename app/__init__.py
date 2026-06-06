import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.extensions import banco
from app.blacklist import BLACKLIST
from app.routes.task import TaskResource
from app.routes.user import UsuarioResource, UserLogin, UserLogout
from app.routes.web import web_bp


def create_app():
    app = Flask(__name__)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    database_path = os.path.join(base_dir, "banco.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "DontTellAnyone"
    app.config["JWT_BLACKLIST_ENABLE"] = True

    banco.init_app(app)

    api = Api(app)
    jwt = JWTManager(app)

    api.add_resource(TaskResource, "/tasks", "/tasks/<int:id_task>")
    api.add_resource(UsuarioResource, "/user", "/user/<int:id_user>")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserLogout, "/logout")

    app.register_blueprint(web_bp)

    @jwt.token_in_blocklist_loader
    def verifica_blacklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLACKLIST

    with app.app_context():
        banco.create_all()

    return app