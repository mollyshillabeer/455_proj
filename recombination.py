#imports
import random

#TODO: how to make this work while ensuring the resulting solution is valid?
# swap only rooms of the same size?
# pick 2 rooms to swap, for the larger room keep only the guests who can't move to smaller one?
def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    
    # student code begin
    #randomly select crossover point
    crossover_point = random.randint(0,len(parent1)-1)
    #preserve 1st part of parents
    offspring1=parent1[:crossover_point]
    offspring2=parent2[:crossover_point]
    #fill rest of offspring with values from opposite parent, starting from
    #after the crossover point then wrapping around to the front
    list1 = parent2[crossover_point:]+parent2[:crossover_point]
    list2 = parent1[crossover_point:]+parent1[:crossover_point]
    for i in list1:
        if i not in offspring1:
            offspring1.append(i)
    for i in list2:
        if i not in offspring2:
            offspring2.append(i)
    # student code end
    return offspring1, offspring2