from forms import ResetPasswordForm, ChangePasswordForm
from flask import Blueprint, render_template, redirect, url_for, flash
import sqlalchemy

from communications.send_email import send_password_reset_email


def create_reset_password_blueprint(app, db, user_model, mail):
    reset_password_bp = Blueprint('reset_password', __name__, template_folder='templates')

    @app.route('/reset_password', methods=['POST', 'GET'])
    def reset_password():
        form = ResetPasswordForm()
        if form.validate_on_submit():
            user = db.session.scalar(sqlalchemy.select(user_model).where(user_model.email == form.email.data))
            if user:
                send_password_reset_email(mail, app, user)
                return redirect(url_for('home_page'))
        return render_template('reset_password.html', title='Reset Password', form=form)

    @app.route('/reset_password_verify/<token>', methods=['POST', 'GET'])
    def reset_password_verify(token):
        user = user_model.verify_reset_password_token(app, db, token)
        form = ChangePasswordForm()
        if form.validate_on_submit():
            user.set_password(form.password.data)
            db.session.commit()
            flash('Your password was changed')
            return redirect(url_for('login'))
        return render_template('change_password.html', form=form)

    return reset_password_bp

