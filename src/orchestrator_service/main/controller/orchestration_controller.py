from flask_restplus import Namespace, Resource
from ..service.orchestration_service import trigger_model_workflow

api = Namespace('orchestration', description='api to trigger full workflow')


@api.route('/')
class OrchestrationTrigger(Resource):
    @api.doc('trigger the full workflow')
    def get(self):
        return trigger_model_workflow()

