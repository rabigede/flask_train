from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired

class userLoginForm(FlaskForm):
    login = StringField("Логин: ", validators=[DataRequired()])
    password = PasswordField("Пароль: ", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")

class newBookForm(FlaskForm):
    name = StringField("Title: ", validators=[DataRequired()])
    author = StringField("Author: ", validators=[DataRequired()])
    submit = SubmitField("Добавить")