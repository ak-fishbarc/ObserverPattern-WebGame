from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

import threading
import time

from forms import ProduceClubForm


def create_unit(username, nosql_db, how_many, how_long):
    timer_done = calculate_time(how_long)
    if timer_done:
        data_exists = nosql_db.cx['player_profiles'][username].find_one({'data': 'clubs'})
        if not data_exists:
            nosql_db.cx['player_profiles'][username].insert_one({'owner': username, 'data': 'clubs',
                                                             'amount': how_many})
        else:
            update_amount = data_exists['amount'] + how_many
            nosql_db.cx['player_profiles'][username].update_one({'data': 'clubs'}, {"$set": {'amount': update_amount}})
    print ('Task complete!')

def calculate_time(how_long):
    time_now = time.time()
    time_then = time.time()
    while (time_then - time_now) < how_long:
        time_then = time.time()
    return True


def create_player_profile_blueprint(app, db, nosql_db, user_model, mail):
    player_profile_bp = Blueprint('player_profile', __name__, template_folder='templates')

    @app.route('/player_profile', methods=['POST', 'GET'])
    def player_profile():
        resources = nosql_db.cx['player_profiles'][current_user.username].find_one({'data': 'resources'})
        return render_template('player_profile.html', title='Profile', resources=resources)

    @app.route('/produce_club/<key>', methods=['POST', 'GET'])
    def produce_club(key):
        max_clubs = 0
        resources = nosql_db.cx['player_profiles'][current_user.username].find_one({'data': 'resources'})
        if int(resources['food'] / 2) != 0 and int(resources['wood'] / 10) != 0:
            how_many_food = int(resources['food'] / 2)
            how_many_wood = int(resources['wood'] / 10)
            if how_many_food <= how_many_wood:
                max_clubs = how_many_food
            elif how_many_wood <= how_many_food:
                max_clubs = how_many_wood
        form = ProduceClubForm()
        if form.validate_on_submit():
            food_cost = form.howmany.data * 2
            wood_cost = form.howmany.data * 10
            resources = nosql_db.cx['player_profiles'][current_user.username].find_one({'data': 'resources'})
            new_value_food = int(resources['food'] - food_cost)
            new_value_wood = int(resources['wood'] - wood_cost)

            nosql_db.cx['player_profiles'][current_user.username].update_one({'data': 'resources'},
                                                                             {"$set": {'food': new_value_food}})

            nosql_db.cx['player_profiles'][current_user.username].update_one({'data': 'resources'},
                                                                             {"$set": {'wood': new_value_wood}})
            print(f"{form.howmany.data} clubs are being produced!")
            t = threading.Thread(target=create_unit, args=(current_user.username, nosql_db, int(form.howmany.data),
                                                           int(form.howmany.data * 10)))
            t.start()
            return redirect(url_for('player_profile'))
        if not key or key != 'Ygplt7XxflI8gO2':
            return "Something went wrong!"
        return render_template('produce_club.html', title="Produce Club", form=form, max_clubs=max_clubs,
                               key='Ygplt7XxflI8gO2')

    return player_profile_bp
