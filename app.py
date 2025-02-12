from flask import Flask, jsonify
from flask_restful import Api
from Resource import task
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, "banco.db")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(task, '/tasks')


if __name__ == '__main__':
    from sqlalchemy import banco
    banco.init_app(app)
    with app.app_context():
        banco.create_all()


    app.run(debug=True)

