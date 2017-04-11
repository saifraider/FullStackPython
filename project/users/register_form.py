from flask_wtf import Form
from wtforms import TextField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired


class RegisterForm(Form):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

