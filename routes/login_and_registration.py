from flask import Blueprint
from flask import render_template, redirect, url_for, flash
import sqlalchemy
from secrets import token_urlsafe

from forms import LoginForm, create_registration_form
from send_email import send_email


def create_login_and_registration_blueprint(app, db, nosql_db, user_model, mail):
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

    @app.route('/register', methods=['POST', 'GET'])
    def register():
        form = create_registration_form(db, user_model)
        if form.validate_on_submit():
            user = user_model(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            verification_token = token_urlsafe(32)
            send_email(mail, "Verify Email", app.config['MAIL_USERNAME'], [form.email.data],
                       render_template("verification_email.html", verification_token=verification_token, username=form.username.data),
                       render_template("verification_email.html", verification_token=verification_token, username=form.username.data))
            db.session.add(user)
            db.session.commit()
            username = form.username.data
            nosql_db.cx['player_profiles'][username].insert_one({'owner': username})
            flash('Registration was successful. Please verify your email address.')
            return redirect(url_for('login'))
        return render_template('register.html', form=form, title="Register")

    @app.route('/verify_email/<username>/<token>')
    def verify_email(username, token):
        if username and token:
            user = db.session.scalar(sqlalchemy. select(user_model).where(user_model.username == username))
            if user and not user.verified:
                user.verify()
                db.session.commit()
                return "Email Verified"
            if user.verified:
                return redirect(url_for('home_page'))
        return "Something went wrong!"

    return login_and_registration_bp

