import os
from flask_script import Manager
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from main import create_app
from orchestrator_service import blueprint


app = create_app(os.getenv('FLASK_MODE') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()
manager = Manager(app)


# @manager.command
# def run():
#     app.run()


if __name__ == '__main__':
    app.run(host='0.0.0.0')


