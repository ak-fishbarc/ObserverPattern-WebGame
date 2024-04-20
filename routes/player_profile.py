from flask import Blueprint, render_template
from flask_login import current_user

from forms import ProduceClubForm


def create_player_profile_blueprint(app, db, nosql_db, user_model, mail):
    player_profile_bp = Blueprint('player_profile', __name__, template_folder='templates')
    
    @app.route('/player_profile', methods=['POST', 'GET'])
    def player_profile():
        resources = nosql_db.cx['player_profiles'][current_user.username].find_one({'data':'resources'})
        form = ProduceClubForm()
        if form.validate_on_submit():
            print("Clubs are being produced!")
        return render_template('player_profile.html', title='Profile', resources=resources)

    @app.route('/produce_club/<key>', methods=['POST', 'GET'])
    def produce_club(key):
        form = ProduceClubForm()
        if not key or key != 'Ygplt7XxflI8gO2':
            return "Something went wrong!"
        return render_template('produce_club.html', title="Produce Club", form=form)

    return player_profile_bp
