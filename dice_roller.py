from random import randint

'''
    Method which rolls a dice a set number of times
    num_sides - int, number of sides that the dice has (d4, d6, d8, etc)
    num_rolls - int, number of times to roll the dice
    modifier - int, value to be added to every roll, can be + or -
    return - list of values with size of num_rolls, each value corresponds to
                a random number between 1 and num_sides + modifier
'''
def rollDice(num_sides, num_rolls, modifier = 0):
    if num_sides < 2:
        sys.exit(f"Error rollDice requires num_sides > 1, you input {num_sides}")
    ret = list()
    for i in range(num_rolls):
        ret.append(randint(1, num_sides) + modifier)    
    return ret
    
'''
    Roll at disadvantage, can only be applied to d20s.
    Rolling with disadvantage means roll twice and take the 
    lowest value
    modifier - int, value to be added to the rolls. Optional input
    return - int, value of the disadvantaged roll
'''
def rollDisadvantage(modifier = 0):
    rolls = rollDice(20, 2, modifier)
    print(rolls)
    if rolls[0] < rolls[1]:
        return rolls[0]
    else:
        return rolls[1]

'''
    Roll at advantage, can only be applied to d20s.
    Rolling with advantage means roll twice and take the 
    highest value
    modifier - int, value to be added to the rolls. Optional input
    return - int, value of the advantaged roll
'''
def rollAdvantage(modifier = 0):
    rolls = rollDice(20, 2, modifier)
    print(rolls)
    if rolls[0] > rolls[1]:
        return rolls[0]
    else:
        return rolls[1]