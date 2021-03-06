from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import session

from src.models.alerts.alert import Alert
from src.models.users.user import User
import src.models.users.errors as UserErrors
import src.models.users.decorators as user_decorators

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for("users.user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/login.jinja2")  # Send user a error if their login was invalid




@user_blueprint.route('/register', methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/register.jinja2")


@user_blueprint.route('/alerts')
@user_decorators.requires_login
def user_alerts():
    user = User.find_by_email(session['email'])
    print str(session['email'])
    alerts = user.get_alerts()
    print str(alert.json() for alert in alerts)
    return render_template('users/alerts.jinja2', alerts=alerts)

@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return redirect( url_for('home') )


@user_blueprint.route('/check_alerts/<string:user_id>')
def check_for_alert(user_id):
    pass
