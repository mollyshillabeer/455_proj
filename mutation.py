import random

#TODO: make sure solution is valid: number of guests can't exceed room size
# could attempt random mutations until one works
# or take advantage of structure, since rooms are ordered by capacity, can easily find 
#the index at which guests can fit within the rooms below it
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
