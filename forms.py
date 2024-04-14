from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import sqlalchemy


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password')
    submit = SubmitField('Log In')


def create_registration_form(db, user_model):

    class RegistrationForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        email = EmailField('Email', validators=[DataRequired(), Email()])
        password = PasswordField('Password', validators=[DataRequired()])
        password2 = PasswordField('Confirm Password', validators=[DataRequired()])
        submit = SubmitField('Register')

        def validate_username(self, username):
            user = db.session.scalar(sqlalchemy.select(user_model).where(user_model.username == username.data))
            if user is not None:
                raise ValidationError('Invalid Username')

        def validate_email(self, email):
            user = db.session.scalar(sqlalchemy.select(user_model).where(user_model.email == email.data))
            if user is not None:
                raise ValidationError('Invalid Email')

    return RegistrationForm()