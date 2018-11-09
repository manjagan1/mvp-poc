from flask import Blueprint
from flask_restplus import Api

from .main.controller.r_training_controller import api as orch_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask R-model training API',
          version='1.0',
          description='Api to train the R model')

api.add_namespace(orch_ns, path='/r_model_training')
