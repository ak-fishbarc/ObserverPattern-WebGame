from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user
import multiprocessing
import time

from forms import ProduceClubForm


def calculate_time(how_long):
    time_now = time.time()
    time_then = time.time()
    while (time_then - time_now) < how_long:
        time_then = time.time()
    print(int(time_then - time_now))


def create_player_profile_blueprint(app, db, nosql_db, user_model, mail):
    player_profile_bp = Blueprint('player_profile', __name__, template_folder='templates')
    
    @app.route('/player_profile', methods=['POST', 'GET'])
    def player_profile():
        resources = nosql_db.cx['player_profiles'][current_user.username].find_one({'data': 'resources'})
        return render_template('player_profile.html', title='Profile', resources=resources)

    @app.route('/produce_club/<key>', methods=['POST', 'GET'])
    def produce_club(key):
        max_clubs = 0
        resources = nosql_db.cx['player_profiles'][current_user.username].find_one({'data':'resources'})
        if int(resources['food']/2) != 0 and int(resources['wood']/10) != 0:
            how_many_food = int(resources['food']/2)
            how_many_wood = int(resources['wood']/10)
            if how_many_food <= how_many_wood:
                max_clubs = how_many_food
            elif how_many_wood <= how_many_food:
                max_clubs = how_many_wood
        form = ProduceClubForm()
        if form.validate_on_submit():
            p = multiprocessing.Process(target=calculate_time, args=((form.howmany.data * 10), ))
            p.start()
            print(f"{form.howmany.data} clubs are being produced!")
            return redirect(url_for('player_profile'))
        if not key or key != 'Ygplt7XxflI8gO2':
            return "Something went wrong!"
        return render_template('produce_club.html', title="Produce Club", form=form, max_clubs=max_clubs, key='Ygplt7XxflI8gO2')

    return player_profile_bp
