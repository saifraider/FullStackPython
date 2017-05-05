from project import create_app
from flask_script import Manager

config_name = 'development'
app = create_app(config_name)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
