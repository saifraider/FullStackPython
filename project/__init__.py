from flask import Flask, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from flask_bootstrap import Bootstrap
from config import secret

app = Flask(__name__)
app.config['SECRET_KEY'] = secret['session_secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:' + secret['postgres_password'] + '@localhost/Flask'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from project.users.views import user_blueprint
from project.home.views import home_blueprint

# register our blueprints
app.register_blueprint(user_blueprint)
app.register_blueprint(home_blueprint)

from models import User

login_manager.login_view = '/login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
