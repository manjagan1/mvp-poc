from flask import Flask
from flask_restplus import Resource, Api
from iofileservice.io_file_service import IOFileService
from datamanipulation.data_manipulation import transform_data

app = Flask(__name__)
api = Api(app)


@api.route('/do_pricing')
class Pricing(Resource):
    def get(self):
        # Retrieve the data from the file system
        data = IOFileService().get_data()

        # Do data manipulations
        transformed_data = transform_data(data)

        print(data.head(10))
        return {'hello': transformed_data['NumberOfOpenCreditLinesAndLoans'].tolist()}




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')