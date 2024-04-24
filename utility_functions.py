import time


def calculate_time(how_long):
    time_now = time.time()
    time_then = time.time()
    while (time_then - time_now) < how_long:
        time_then = time.time()

    return True


# Calculates max number of units that can be produced based on:
# 1. How much food and wood is available.
# 2. The cost of the unit.
# Returns 0 if there's not enough resources.
def calculate_max_number_of_units(food_cost, wood_cost, resources_food, resources_wood):
    max_units = 0

    if int(resources_food / food_cost) != 0 and int(resources_wood / wood_cost) != 0:
        how_much_food = int(resources_food / food_cost)
        how_much_wood = int(resources_wood / wood_cost)
        """ 
            Pick the lowest possible value for max_units based on resources/cost.
            E.g: If we have 20 food and 50 wood and the unit costs 2 food and 10 wood:
            1. We could make 10 units based on food and 5 units based on wood. 
            2. In that case we can make only 5 units using 10 food and 50 wood.
        """
        if how_much_food <= how_much_wood:
            max_units = how_much_food
        elif how_much_wood <= how_much_food:
            max_units = how_much_wood

    return max_units

