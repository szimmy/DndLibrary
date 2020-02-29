from random import randint


def roll_dice(num_sides, num_rolls, modifier=0, print_values=False):
    """ 
    Method which rolls a dice a set number of times
    num_sides - int, number of sides that the dice has (d4, d6, d8, etc)
    num_rolls - int, number of times to roll the dice
    modifier - int, value to be added to every roll, can be + or -
    print_values - bool, print the items to be returned as well as return them. Optional input
    return - list of values with size of num_rolls, each value corresponds to
                a random number between 1 and num_sides + modifier
    """
    if num_sides < 2:
        raise ValueError(
            f"Error roll_dice requires num_sides > 1, you input {num_sides}"
        )

    ret = []
    for i in range(num_rolls):
        ret.append(randint(1, num_sides) + modifier)

    if print_values:
        print(ret)

    return ret


def roll_disadvantage(num_sides=20, modifier=0, print_value=False):
    """
    Rolling with disadvantage means roll twice and take the 
    lowest value
    num_sides - int, number of sides that the dice has (d4, d6, d8, etc)
    modifier - int, value to be added to the rolls. Optional input
    print_value - bool, print the item to be returned as well as return them. Optional input
    return - int, value of the disadvantaged roll
    """
    rolls = roll_dice(20, 2, modifier)
    ret = min(rolls)

    if print_value:
        print(ret)

    return ret


def roll_advantage(num_sides=20, modifier=0, print_value=False):
    """
    Rolling with advantage means roll twice and take the 
    highest value
    num_sides - int, number of sides that the dice has (d4, d6, d8, etc)
    modifier - int, value to be added to the rolls. Optional input
    print_value - bool, print the item to be returned as well as return them. Optional input
    return - int, value of the advantaged roll
    """
    rolls = roll_dice(20, 2, modifier)
    ret = max(rolls)

    if print_value:
        print(ret)

    return ret
