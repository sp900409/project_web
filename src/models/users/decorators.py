from functools import wraps

from flask import redirect
from flask import request
from flask import session
from flask import url_for
from src.app import app

def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # all decorator into decorated_function
        # below is addition part of decorator add to original function
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next = request.path))
        return func(*args, **kwargs)   # func(...) args : function argument
    return decorated_function


def requires_admin_permission(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # all decorator into decorated_function
        # below is addition part of decorator add to original function
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next = request.path))
        if session['email'] not in app.config['ADMINS']:
            return redirect(url_for('users.login_user', message="you need to be a admin"))
        return func(*args, **kwargs)   # func(...) args : function argument
    return decorated_function


