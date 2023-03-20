#imports
from itertools import permutations
import random

#TODO: this needs serious modification to make valid permutations and include specific data
#use hotel and guest classes
def permutation (pop_size, chrom_length):
    """initialize a population of permutation"""

    population = []
    # student code begin
    # each individual is represented by a list of integers from 1 to 8
    chrom = list(range(1,chrom_length+1))
    #randomly select initial population from all possible solutions
    population = random.sample(list(permutations(chrom)),pop_size)
    population = [list(t) for t in population] #convert from tuple to list
    #student code end
    return population