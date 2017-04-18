from project import create_app
from flask.ext.script import Manager

app = create_app('development')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
