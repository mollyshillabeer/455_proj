# imports
import random
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import product

# import your own modules
import initialization
import evaluation
import parent_selection
import recombination
import mutation
import survivor_selection
import other_approaches


#TODO: parameter control, probability of room getting destroyed, swap clients in and out from hotel

def visualization(maxes,avgs,guests):
    #plot max fitness per generation
    ax = sns.lineplot(data=maxes)
    ax.set(xlabel="generation",ylabel="fitness",title="Max Fitness by Generation")
    plt.show()
    
    #plot average fitness per generation
    ax1 = sns.lineplot(data=avgs)
    ax1.set(xlabel="generation",ylabel="fitness",title="Average Fitness by Generation")
    plt.show()
    
    #histogram of guest sizes and durations - demonstrating properties of guest dataset
    sizes = [a.size for a in guests]
    ax2 = sns.histplot(data=sizes)
    ax2.set(xlabel="size",ylabel="num reservations",title="Distribution of Reservation Sizes")
    plt.show()
    
    durations = [a.num_days for a in guests]
    ax3 = sns.histplot(data=durations)
    ax3.set(xlabel="length of stay",ylabel="num reservations",title="Distribution of Reservation Sizes")
    plt.show()

def main(pop_size,mating_pool_size,tournament_size,xover_rate,mut_rate,gen_limit,verbose=True):
    random.seed()
    numpy.random.seed()

    #parameters set by the hotel requirements 
    num_guests = 70 #should be multiples of 14
    num_guests_per_room = 5
    max_days = 3000 #number of days the hotel is booking for
    #other parameters are set by the calling function, were tuned through hyperparameter control

    # initialize population and starting fitness values
    gen = 0 # initialize the generation counter
    population, backups, hotel, guests = initialization.permutation(pop_size, num_guests, num_guests_per_room)
    fitness = []
    for i in range (0, pop_size):
        fitness.append(evaluation.fitness(population[i], hotel, guests, max_days))

    if verbose:
        print("generation", gen, ": best fitness", max(fitness), "\taverage fitness", sum(fitness)/len(fitness))

    max_fitnesses = []
    avg_fitnesses = []
    # evolution begins, stopping criteria is a limit on number of generations
    while gen < gen_limit:
        #pick parents 
        #parents_index = parent_selection.MPS(fitness, mating_pool_size)
        parents_index = parent_selection.tournament(fitness, mating_pool_size, tournament_size)

        #shuffle parents to randomly pair them up
        random.shuffle(parents_index)
    
        #reproduction: make offspring with recombination and mutate them, then calculate their fitnesses
        offspring =[]
        offspring_fitness = []
        i= 0 # initialize the counter for parents in the mating pool
        # offspring are generated using selected parents in the mating pool
        while len(offspring) < mating_pool_size:
        
            #recombination
            if random.random() < xover_rate:            
                off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]], hotel, guests)
            else:
                off1 = population[parents_index[i]].copy()
                off2 = population[parents_index[i+1]].copy()

            #mutation
            if random.random() < mut_rate:
                off1 = mutation.permutation_swap(off1,hotel,guests)
            if random.random() < mut_rate:
                off2 = mutation.permutation_swap(off2,hotel,guests)
        
            offspring.append(off1)
            offspring_fitness.append(evaluation.fitness(off1, hotel, guests, max_days))
            offspring.append(off2)
            offspring_fitness.append(evaluation.fitness(off2, hotel, guests, max_days))
            i+=2  # update the counter

        #survivour selection to make the population of next generation
        #population, fitness = survivor_selection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
        population, fitness = survivor_selection.replacement(population, fitness, offspring, offspring_fitness)
        
        gen += 1  # update the generation counter
        
        #calculate overall fitness values for the population
        if verbose:
            print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))
        max_fitnesses.append(max(fitness))
        avg_fitnesses.append(sum(fitness)/len(fitness))

    # evolution ends
    # print the final best solution(s)
    if verbose:
        k = 0
        for i in range (0, pop_size):
            if fitness[i] == max(fitness):
                print("best solution", k, population[i], fitness[i])
                k += 1
        #visualize results
        visualization(max_fitnesses,avg_fitnesses,guests)
        #compare to alternate approach
        print("greedy solution and fitness: "+str(other_approaches.greedy(num_guests, num_guests_per_room, max_days, guests, hotel)))
    return max(fitness)

def param_tuning():
    '''
    Grid search for parameter tuning. Every possible option is attempted.
    Final max fitness is compared and the best one is printed out.
    '''
    print("Tuning Now")
    pop_size = [50, 70, 100] 
    #int(pop_size*0.5)
    mating_pool_size = [20, 30, 50] # has to be even
    tournament_size = [4,6,10]
    xover_rate = [0.1, 0.3, 0.5, 0.7, 0.9]
    mut_rate = [0.1, 0.3, 0.5, 0.7, 0.9]
    gen_limit = [50, 75, 100, 125, 150]
    params = product(pop_size,mating_pool_size,tournament_size,xover_rate,mut_rate,gen_limit)
    
    #track best option
    max_fit = 0
    max_arr = ()
    for arr in params:
        fitness = main(*arr,verbose=False)
        if fitness >= max_fit:
            max_fit=fitness
            max_arr=arr
    print("Params: "+str(max_arr)+" Fitness: "+str(max_fit))
    
def stats(num_tries):
    '''
    Run the EA n times and calculate various metrics to evaluate success.
    - Average max fitness
    '''
    fitnesses=[]
    for i in range(num_tries):
        fitness = main(50,50,10,0.9,0.5,150,verbose=False)
        fitnesses.append(fitness)
    print("Average Max Fitness: "+str(sum(fitnesses)/len(fitnesses)))