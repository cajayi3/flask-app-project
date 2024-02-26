from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
class UserLoginForm(FlaskForm):
    # email, password, submit
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField('Post')
