from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import session

from src.models.users.user import User
import src.models.users.errors as UserErrors

user_blueprint = Blueprint('User', __name__)


# class UserErrors(object):
#     pass


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/login.html")  # Send user a error if their login was invalid






@user_blueprint.route('/register')
def register_user():
    pass


@user_blueprint.route('/alerts')
def user_alerts():
    return "This is the alert page"

@user_blueprint.route('/logout')
def logout_user():
    pass

@user_blueprint.route('/check_alerts/<string:user_id>')
def check_for_alert(user_id):
    pass
