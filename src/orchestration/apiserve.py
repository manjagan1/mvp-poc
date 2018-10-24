from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/do_pricing')
class Pricing(Resource):
    def get(self):
        fileSystem = FileSystemAccess()
        return {'hello': 'world'}


class FileSystemAccess():

    # get the path of the files in the filesystem
    # TODO : later change this to get the data file path from the config.ini
    @staticmethod
    def get_path():
        path = "../data/"
        return path

    def get_csv_file(self, filename = "transactions.csv"):
        csv_file_path = get_path()




if __name__ == '__main__':
    app.run(debug=True)