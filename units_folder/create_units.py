from communications.notifications import send_notification
from utility_functions import calculate_time


# Unit creation function that waits for the timer to finish, then creates/updates User's
# file in MongoDB with the amount of units that was produced.
def create_unit(username, nosql_db, notify, unit_name, how_many, how_long):
    unit_to_make = {'data': unit_name}
    timer_done = calculate_time(how_long)

    if timer_done:
        data_exists = nosql_db.cx['player_profiles'][username].find_one(unit_to_make)
        if not data_exists:
            nosql_db.cx['player_profiles'][username].insert_one({'owner': username, 'data': unit_name,
                                                                'amount': how_many})
        else:
            update_amount = data_exists['amount'] + how_many
            nosql_db.cx['player_profiles'][username].update_one(unit_to_make, {"$set": {'amount': update_amount}})
    if notify:
        send_notification('Clubs are ready', 'Check out your new clubs!')
    print('Task complete!')

