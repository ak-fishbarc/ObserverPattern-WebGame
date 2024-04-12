from flask import Blueprint
from flask import render_template


def create_login_and_registration_blueprint():
    login_and_registration = Blueprint('login_and_registration', __name__, template_folder='templates')

    @login_and_registration.route('/login')
    def login():
        return render_template('login.html', title="Login")

    return login_and_registration
