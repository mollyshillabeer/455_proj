# imports
import random
import decimal

# mating pool size is lamba

def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""
    selected_to_mate = [] 
    sumOfFitnesses = sum(fitness)
    a = [fitness[0]/sumOfFitnesses] # start with the first value in the list
    for i in range (1,len(fitness)): # start with the second value in the list
        x = fitness[i]/sumOfFitnesses
        a.append(x + a[i-1])
    len(selected_to_mate) = 1
    i = 0
    r = random.uniform(0, 1/mating_pool_size)
    while(len(selected_to_mate) <= mating_pool_size):
        while (r <= a[i]):
            selected_to_mate.append(i)# select the indexes 
            r = r + 1/mating_pool_size
            len(selected_to_mate) = len(selected_to_mate) + 1
        i = i + 1
    return selected_to_mate

def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""
    # tournament_size is k
    selected_to_mate = []
    len(selected_to_mate) = 0
    while (len(selected_to_mate) <= mating_pool_size):
        k = random.choices(fitness,k =tournament_size)
        i = fitness.index(max(k))
        selected_to_mate.append(i)
        len(selected_to_mate) = len(selected_to_mate) + 1
    return selected_to_mate

def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""
    selected_to_mate = []
    list1 = list(range(population_size))
    selected_to_mate += random.sample(list1, mating_pool_size)
    return selected_to_mate
