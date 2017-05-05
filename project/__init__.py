from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table
from flask_bootstrap import Bootstrap
from config import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

bootstrap = Bootstrap()
# db = SQLAlchemy()
login_manager = LoginManager()
Base = declarative_base()
session = None
metadata = None


def create_app(config_name):
    global session

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    session, engine = loadSession(config[config_name].SQLALCHEMY_DATABASE_URI)

    bootstrap.init_app(app)
    # db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = '/login'

    from project.users.views import user_blueprint
    app.register_blueprint(user_blueprint)

    from project.home.views import home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/home')

    from project.models.users import User,Timepass

    Base.metadata.create_all(bind=engine)

    # with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........


    # db.create_all()


    @login_manager.user_loader
    def load_user(user_id):
        return session.query(User).filter(User.id == int(user_id)).first()

    return app


def loadSession(uri):
    global metadata
    global session

    engine = create_engine(uri)
    metadata = MetaData(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session, engine
