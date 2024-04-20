from flask import Blueprint, render_template

from forms import ProduceClubForm


def create_player_profile_blueprint(app, db, user_model, mail):
    player_profile_bp = Blueprint('player_profile', __name__, template_folder='templates')
    
    @app.route('/player_profile')
    def player_profile():
        return render_template('player_profile.html', title='Profile')

    @app.route('/produce_club/<key>')
    def produce_club(key):
        form = ProduceClubForm()
        if not key or key != 'Ygplt7XxflI8gO2':
            return "Something went wrong!"
        return render_template('produce_club.html', title="Produce Club", form=form)

    return player_profile_bp
