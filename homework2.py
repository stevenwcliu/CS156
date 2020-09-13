# ----------------------------------------------------------------------
# Name:        homework2
# Purpose:     Practice writing Python functions
#
# Author(s): Wencong Liu(Steven), Yi-En Laih(Emily)
# Team Name: Mustard Seed
# ----------------------------------------------------------------------
"""
Implement functions to track Sammy's consumption of carrots.
Sammy is an eco-friendly intelligent agent powered by carrots.
His task is to collect medals at various positions in a grid.
Sammy can only move North, South, West or East.
The carrot consumption per step for each direction is given by a
dictionary that is passed to the various functions.
The functions must work with any dictionary specifying the carrot
consumption.
"""

# Constants
NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"


def carrots_to_medal(sammy, medal, carrot_cost):
    """
    Compute the number of carrots that  Sammy consumes to reach the
    given medal.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medal (tuple) representing the position of a given medal
    :param carrot_cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (integer) the number of carrots.
    """
    # Enter your code here and remove the pass statement below
    sam_x, sam_y = sammy
    med_x, med_y = medal

    horizontal_cost = 0
    vertical_cost = 0
    if sam_x > med_x:
        horizontal_cost = (sam_x - med_x) * carrot_cost[WEST]
        # print(west_cost)
    elif med_x > sam_x:
        horizontal_cost = (med_x - sam_x) * carrot_cost[EAST]

    if sam_y > med_y:
        vertical_cost = (sam_y - med_y) * carrot_cost[NORTH]
        # print(west_cost)
    elif med_y > sam_y:
        vertical_cost = (med_y - sam_y) * carrot_cost[SOUTH]

    return horizontal_cost + vertical_cost


def min_carrots(sammy, medals, carrot_cost):
    """
    Compute the minimum number of carrots that Sammy consumes to reach a
    medal.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medals (set of tuples) containing the positions of all medals
    :param carrot_cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (integer) the number of carrots.
    """
    # use generator expression + min function and if medal is empty return None
    if not medals:
        return None
    if medals:
        carrot_cost = min(carrots_to_medal(sammy, medal, carrot_cost) for medal in medals)
        return carrot_cost


def most_carrots_medal(sammy, medals, carrot_cost):
    """
    Find the medal that Sammy consumes the most carrots to reach.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medals (set of tuples) containing the positions of all medals
    :param carrot_cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (tuple) the position of the medal
    """

    # must use max function with a key that is a lambda function
    if not medals:
        return None
    if medals:
        # carrot_cost = max(carrots_to_medal(sammy, medal, carrot_cost) for medal in medals)
        pos = max(medals, key=lambda p: carrots_to_medal(sammy, p, carrot_cost))
        return pos


def main():
    # The main function is used to test the 3 functions.
    carrot_cost1 = {WEST: 1, EAST: 2, SOUTH: 3, NORTH: 4}
    sammy1 = (10, 3)
    print('----------Testing the carrots_to_medal function----------')
    print(carrots_to_medal(sammy1, (3, 1), carrot_cost1))  # 15
    print(carrots_to_medal(sammy1, (0, 8), carrot_cost1))  # 25
    print(carrots_to_medal(sammy1, (10, 6), carrot_cost1))  # 9
    print(carrots_to_medal(sammy1, (14, 3), carrot_cost1))  # 8
    print(carrots_to_medal(sammy1, (13, 7), carrot_cost1))  # 18
    print(carrots_to_medal(sammy1, (10, 3), carrot_cost1))  # 0
    print('----------')
    sammy2 = (2, 2)
    carrot_cost2 = {NORTH: 1, EAST: 2, WEST: 3, SOUTH: 4}
    print(carrots_to_medal(sammy2, (3, 1), carrot_cost2))  # 3
    print(carrots_to_medal(sammy2, (0, 8), carrot_cost2))  # 30
    print(carrots_to_medal(sammy2, (10, 6), carrot_cost2))  # 32
    print(carrots_to_medal(sammy2, (14, 3), carrot_cost2))  # 28
    print(carrots_to_medal(sammy2, (13, 7), carrot_cost2))  # 42
    print(carrots_to_medal(sammy2, (10, 3), carrot_cost2))  # 20
    print('----------Testing the min_carrots function----------')
    medals1 = {(3, 1), (0, 8), (13, 7), (1, 4), (10, 6), (14, 3)}
    medals2 = {(10, 3), (14, 3), (13, 7)}
    print(min_carrots(sammy1, medals1, carrot_cost1))  # 8
    print(min_carrots(sammy1, {}, carrot_cost1))  # None
    print(min_carrots(sammy1, medals2, carrot_cost1))  # 0
    print(min_carrots(sammy2, medals1, carrot_cost2))  # 3
    print(min_carrots(sammy2, {}, carrot_cost2))  # None
    print(min_carrots(sammy2, medals2, carrot_cost2))  # 20
    print('-------Testing the most_carrots_medal function-------')
    print(most_carrots_medal(sammy1, medals1, carrot_cost1))  # (0, 8)
    print(most_carrots_medal(sammy1, {}, carrot_cost1))  # None
    print(most_carrots_medal(sammy1, medals2, carrot_cost1))  # (13, 7)
    print(most_carrots_medal(sammy1, medals2, carrot_cost2))  # (13, 7)


if __name__ == '__main__':
    main()