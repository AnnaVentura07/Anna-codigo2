from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Deixa o banco de dados pronto, mas ainda não ligou no app
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Diz pro Flask onde o arquivo do banco vai ficar guardado
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_projeto.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Agora sim: conecta o banco com o nosso app
    db.init_app(app)

    # Espaço reservado pra puxar as rotas (os caminhos do site) depois
    # from .routes import main
    # app.register_blueprint(main)

    return app