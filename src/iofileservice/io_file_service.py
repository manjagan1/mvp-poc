from flask import Flask
from flask_restplus import Api

api = Api()

app = Flask(__name__)
api.init_app(app)