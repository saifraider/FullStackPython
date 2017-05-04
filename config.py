import os

class Config:
    SECRET_KEY = os.environ.get('SESSION_SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:' + POSTGRES_PASSWORD + '@localhost/Flask'
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


# class ProductionConfig(Config):
#    not decided yet

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
    # 'production':ProductionConfig
}
