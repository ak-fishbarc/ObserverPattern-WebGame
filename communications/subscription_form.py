from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField


class SubscriptionForm(FlaskForm):
    subscribe = BooleanField('Subscribe')
    submit = SubmitField('Subscribe')
