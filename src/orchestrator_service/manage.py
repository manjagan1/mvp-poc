import os
from flask_script import Manager
from main import create_app

app = create_app(os.getenv('FLASK_MODE') or 'dev')
app.app_context.push()
manager = Manager(app)


@manager.add_command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()


