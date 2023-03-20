# imports
import random
import numpy

# import your own modules
import initialization
import evaluation
import parent_selection
import recombination
import mutation
import survivor_selection


#TODO: parameter control

def main():
    random.seed()
    numpy.random.seed()

    string_length = 8  # may extend to N queens
    popsize = 20  
    mating_pool_size = int(popsize*0.5) # has to be even
    tournament_size = 4
    xover_rate = 0.9
    mut_rate = 0.2
    gen_limit = 50

    # initialize population
    gen = 0 # initialize the generation counter
    population = initialization.permutation(popsize, string_length)
    fitness = []
    for i in range (0, popsize):
        fitness.append(evaluation.fitness_8queen(population[i]))
    print("generation", gen, ": best fitness", max(fitness), "\taverage fitness", sum(fitness)/len(fitness))

    # evolution begins
    while gen < gen_limit:
        
        # pick parents 
        parents_index = parent_selection.MPS(fitness, mating_pool_size)
        #parents_index = parent_selection.tournament(fitness, mating_pool_size, tournament_size)

        # in order to randomly pair up parents
        random.shuffle(parents_index)
    
        # reproduction
        offspring =[]
        offspring_fitness = []
        i= 0 # initialize the counter for parents in the mating pool
        
        # offspring are generated using selected parents in the mating pool
        while len(offspring) < mating_pool_size:
        
            # recombination
            if random.random() < xover_rate:            
                off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]])
            else:
                off1 = population[parents_index[i]].copy()
                off2 = population[parents_index[i+1]].copy()

            # mutation
            if random.random() < mut_rate:
                off1 = mutation.permutation_swap(off1)
            if random.random() < mut_rate:
                off2 = mutation.permutation_swap(off2)
        
            offspring.append(off1)
            offspring_fitness.append(evaluation.fitness_8queen(off1))
            offspring.append(off2)
            offspring_fitness.append(evaluation.fitness_8queen(off2))
            i = i+2  # update the counter

        # organize the population of next generation
        population, fitness = survivor_selection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
        #population, fitness = survivor_selection.replacement(population, fitness, offspring, offspring_fitness)
        
        gen += 1  # update the generation counter
        print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))
        
    # evolution ends
    # print the final best solution(s)
    k = 0
    for i in range (0, popsize):
        if fitness[i] == max(fitness):
            print("best solution", k, population[i], fitness[i])
            k = k+1

main()