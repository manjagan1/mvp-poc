from flask_restplus import Namespace, Resource
from ..service.r_training_service import boilerplate_service

api = Namespace('r-model-trainind', description='api to train R model')


@api.route('/')
class BoilerplateEndpoint(Resource):
    @api.doc('R-model-training endpoint')
    def get(self):
        return boilerplate_service()

