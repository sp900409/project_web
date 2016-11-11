from flask import Blueprint


alert_blueprint = Blueprint('alerts', __name__)

@alert_blueprint.route('/')
def index():
    return "this is alerts index"

@alert_blueprint.route('/new', methods=['post'])
def create_alert():
    pass


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactive_alert(alert_id):
    pass


@alert_blueprint.route('/alert/<string:alert_id>')
def get_alert_page(alert_id):
    pass


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alert_for_user(user_id):
    pass
