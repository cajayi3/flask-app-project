from flask import Flask
from .auth.routes import auth
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app)


app.register_blueprint(auth)

app.config.from_object(Config)