from flask_restplus import Namespace, Resource
from ..service.orchestration_service import trigger_io_fileservice, trigger_model

api = Namespace('orchestration', description='api to trigger full workflow', path='/orchestration')


@api.route('/')
class OrchestrationTrigger(Resource):
    @api.doc('trigger the full workflow')
    def get(self):
        # Call ReWrMo
        trigger_io_fileservice()

        # Call R model
        trigger_model()

        # Call last man

