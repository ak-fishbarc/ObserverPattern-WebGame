from flask import Blueprint
from flask import render_template


def create_login_and_registration_blueprint():
    login_and_registration_bp = Blueprint('login_and_registration', __name__, template_folder='templates')

    @login_and_registration_bp.route('/login')
    def login():
        return render_template('login.html', title="Login")

    @login_and_registration_bp.route('/register')
    def register():
        return render_template('register.html', title="Register")

    return login_and_registration_bp
