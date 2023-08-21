from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///comunidade.db'
# para o banco de dados postgre do Render
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# para criar o banco de dados no Render usando o arquivo criar_banco.py
# app.config["SQLALCHEMY_DATABASE_URI"] = 'EXTERNAL RENDER DATABASE URL' -> Lembrar de acrescenter o sql no postgres
app.config["SECRET_KEY"] = 'e0c74f0b225bab72ff51fdf54af426c6'
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

from fakepinterest import routes
