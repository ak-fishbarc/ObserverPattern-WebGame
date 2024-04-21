from flask_wtf import FlaskForm
from wtforms import DecimalRangeField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class ProduceClubForm(FlaskForm):
    howmany = DecimalRangeField('How many?', validators=[DataRequired()])
    notify_me = BooleanField('Notify')
    submit = SubmitField('Create Clubs')

