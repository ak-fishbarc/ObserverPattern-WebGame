from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
import threading

from units_folder.units_forms import ProduceClubForm
from units_folder.create_units import create_unit
from units_folder.units_templates import club
from utility_functions import calculate_max_number_of_units


def create_player_pages_blueprint(app, db, nosql_db, user_model, mail):
    player_profile_bp = Blueprint('player_profile', __name__, template_folder='templates')

    @app.route('/player_profile/<player>')
    @login_required
    def player_profile(player):
        return render_template('player_profile.html', title='Profile')

    @app.route('/game_display/<player>', methods=['POST', 'GET'])
    @login_required
    def game_display(player):
        resources = nosql_db.cx['player_profiles'][player].find_one({'data': 'resources'})
        return render_template('game_display.html', title='Game Window', resources=resources)

    @app.route('/produce_club/<key>', methods=['POST', 'GET'])
    def produce_club(key):
        user_name = current_user.username
        dict_res = {'data': 'resources'}
        resources = nosql_db.cx['player_profiles'][user_name].find_one(dict_res)
        res_food = resources['food']
        res_wood = resources['wood']
        max_clubs = calculate_max_number_of_units(club['food_cost'], club['wood_cost'], res_food, res_wood)

        form = ProduceClubForm()
        if form.validate_on_submit():
            form_data = form.howmany.data
            food_cost = form_data * club['food_cost']
            wood_cost = form_data * club['wood_cost']
            new_value_food = int(res_food - food_cost)
            new_value_wood = int(res_wood - wood_cost)

            nosql_db.cx['player_profiles'][user_name].update_one(dict_res,
                                                                 {"$set": {'food': new_value_food}})

            nosql_db.cx['player_profiles'][user_name].update_one(dict_res,
                                                                 {"$set": {'wood': new_value_wood}})
            print(f"{form_data} clubs are being produced!")
            t = threading.Thread(target=create_unit, args=(user_name, nosql_db, form.notify_me.data, 'clubs',
                                                           int(form_data), int(form_data * 10)))
            t.start()
            return redirect(url_for('player_profile'))
        if not key or key != 'Ygplt7XxflI8gO2':
            return "Something went wrong!"
        return render_template('produce_club.html', title="Produce Club", form=form, max_clubs=max_clubs,
                               key='Ygplt7XxflI8gO2')

    return player_profile_bp

