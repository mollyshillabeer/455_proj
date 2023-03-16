import random

def permutation_swap (individual):
    """Mutate a permutation"""
     
    mutant = individual.copy()
    
    val1 = random.choice(mutant)
    val2 = random.choice(mutant)
    val1Position = mutant.index(val1)
    val2Position = mutant.index(val2)
    mutant[val1Position] = val2
    mutant[val2Position] = val1
    
    return mutant
