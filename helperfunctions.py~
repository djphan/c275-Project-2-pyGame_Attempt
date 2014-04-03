import random

def randomizer_output(items):
    """
    randomizer_output takes in a list of tuples (items) of the following format: (item, weight) 
    and returns the item at a given probability. For this assignment this will be
    [(-1, 0.2), (0, 0.5), (1, 0.2), (2, 0.2)]
 
    To call final damage we will need to output the following value
    final_damage = max((initial_damage + randomizer_output([(-1, 0.2), (0, 0.5), (1, 0.2), (2, 0.1)])), 0)
    """
    total_probability = sum(item[1] for item in items)
    n = random.uniform(0, total_probability)
    for item, weight, in items:
        if n < weight:
            return item
        n = n - weight
    return item
