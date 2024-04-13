from flask import Blueprint
from flask import render_template, redirect, url_for, flash
import sqlalchemy

from forms import LoginForm


def create_login_and_registration_blueprint(app, db, user_model):
    login_and_registration_bp = Blueprint('login_and_registration', __name__, template_folder='templates')

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = db.session.scalar(sqlalchemy.select(user_model).where(user_model.username == form.username.data))
            if user is None:
                flash('Invalid username')
                return redirect(url_for('login'))
            return redirect(url_for('home_page'))
        return render_template('login.html', form=form, title="Login")

    @app.route('/register')
    def register():
        return render_template('register.html', title="Register")

    return login_and_registration_bp

