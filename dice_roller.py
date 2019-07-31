from random import randint

'''
    Method which rolls a dice a set number of times
    num_sides - int, number of sides that the dice has (d4, d6, d8, etc)
    num_rolls - int, number of times to roll the dice
    modifier - int, value to be added to every roll, can be + or -
    print_values - bool, print the items to be returned as well as return them. Optional input
    return - list of values with size of num_rolls, each value corresponds to
                a random number between 1 and num_sides + modifier
'''
def rollDice(num_sides, num_rolls, modifier = 0, print_values = False):
    if num_sides < 2:
        sys.exit(f"Error rollDice requires num_sides > 1, you input {num_sides}")
    ret = list()
    for i in range(num_rolls):
        ret.append(randint(1, num_sides) + modifier)    
    if print_values:
        print(ret)
    return ret
    
'''
    Roll at disadvantage, can only be applied to d20s.
    Rolling with disadvantage means roll twice and take the 
    lowest value
    modifier - int, value to be added to the rolls. Optional input
    print_value - bool, print the item to be returned as well as return them. Optional input
    return - int, value of the disadvantaged roll
'''
def rollDisadvantage(modifier = 0, print_value = False):
    rolls = rollDice(20, 2, modifier)
    ret = rolls[1]
    if rolls[0] < rolls[1]:
        ret = rolls[0]
    if print_value:
        print(ret)
    return ret

'''
    Roll at advantage, can only be applied to d20s.
    Rolling with advantage means roll twice and take the 
    highest value
    modifier - int, value to be added to the rolls. Optional input
    print_value - bool, print the item to be returned as well as return them. Optional input
    return - int, value of the advantaged roll
'''
def rollAdvantage(modifier = 0, print_value = False):
    rolls = rollDice(20, 2, modifier)
    ret = rolls[1]
    if rolls[0] > rolls[1]:
        ret = rolls[0]
    if print_value:
        print(ret)
    return ret