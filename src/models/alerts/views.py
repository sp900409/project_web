from flask import Blueprint
from flask import render_template

alert_blueprint = Blueprint('alerts', __name__)

@alert_blueprint.route('/')
def index():
    return render_template('alerts/alert.jinja2')

@alert_blueprint.route('/new', methods=['post'])
def create_alert():
    pass


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactive_alert(alert_id):
    pass


@alert_blueprint.route('/<string:alert_id>')
def get_alert_page(alert_id):
    return render_template('alert/alert.jinja2')


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alert_for_user(user_id):
    pass
