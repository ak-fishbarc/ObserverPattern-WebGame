import time


def calculate_time(how_long):
    time_now = time.time()
    time_then = time.time()
    while (time_then - time_now) < how_long:
        time_then = time.time()

    return True


def calculate_max_number_of_units(food_cost, wood_cost, resources_food, resources_wood):
    max_units = 0

    if int(resources_food / food_cost) != 0 and int(resources_wood / wood_cost) != 0:
        how_many_food = int(resources_food / food_cost)
        how_many_wood = int(resources_wood / wood_cost)
        if how_many_food <= how_many_wood:
            max_units = how_many_food
        elif how_many_wood <= how_many_food:
            max_units = how_many_wood

    return max_units

