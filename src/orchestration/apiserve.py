from flask import Flask
from flask_restplus import Resource, Api
import sys
import os

# sys.path.append(os.path.dirname(__file__))
# from src.orchestration.iofileservice.io_file_service import IOFileService
# from iofileservice.io_file_service import IOFileService


app = Flask(__name__)
api = Api(app)


@api.route('/do_pricing')
class Pricing(Resource):
    def get(self):
        # data = IOFileService()
        return {'hello': 'world'}




if __name__ == '__main__':
    app.run(debug=True)