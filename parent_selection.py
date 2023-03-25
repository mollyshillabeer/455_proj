# imports
import random
import decimal

# mating pool size is lamba

def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""
    selected_to_mate = []

    # student code starts
    # 1st make the probability distribution, saving the top boundaries 
    # for each individual's section of the wheel. ranges from 0 to 1
    wheel = []
    total = sum(fitness)
    top = 0
    for i in fitness:
        f = i/total
        wheel.append(top+f)
        top += f
    step_size = 1.0/mating_pool_size
    #randomly choose spot to start
    r = random.uniform(0,step_size)
    i = 0
    current_member = 0
    # while not all parents are selected, increment r by the step size, 
    # adding the individual whose distribution the r value is in
    # individuals with slices larger than the step size can be picked multiple times
    while current_member < mating_pool_size:
        while r <= wheel[i]:
            selected_to_mate.append(i)
            r+=step_size
            current_member+=1
        i+=1
    return selected_to_mate

def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""
    selected_to_mate = []
    # student code starts
    pop_size = len(fitness)
    current_member = 0
    # while not all parents are selected, perform tournaments to pick parents 1 at a time
    while current_member < mating_pool_size:
        #randomly select individuals for tournament, without replacement
        tournament_members = random.sample(range(pop_size),tournament_size)
        fitnesses_of_tournament = [fitness[index] for index in tournament_members]
        winner = max(fitnesses_of_tournament)
        #add the index of the winner to the list of parents
        i = tournament_members[fitnesses_of_tournament.index(winner)]
        selected_to_mate.append(i)
        current_member+=1
    # student code ends
    return selected_to_mate
