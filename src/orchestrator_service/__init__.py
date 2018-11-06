from flask import Blueprint
from flask_restplus import Api

from .main.controller.orchestration_controller import api as orch_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask Orchestrator Service',
          version='1.0',
          description='Api for triggering the whole modelling workflow')

api.add_namespace(orch_ns, path='/orchestration')
