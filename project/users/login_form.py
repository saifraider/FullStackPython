
from flask_wtf import Form
from wtforms import TextField, PasswordField, StringField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired


class LoginForm(Form):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')