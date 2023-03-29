# imports
import random
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

# import your own modules
import initialization
import evaluation
import parent_selection
import recombination
import mutation
import survivor_selection


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

def main():
    random.seed()
    numpy.random.seed()

    #parameters
    num_guests = 28 #should be multiples of 14
    num_guests_per_room = 2
    pop_size = 20  
    mating_pool_size = int(pop_size*0.5) # has to be even
    tournament_size = 4
    xover_rate = 0.9
    mut_rate = 0.2
    gen_limit = 50
    max_days = 3000 #number of days the hotel is booking for

    # initialize population
    gen = 0 # initialize the generation counter
    population, backups, hotel, guests = initialization.permutation(pop_size, num_guests, num_guests_per_room)
    fitness = []
    for i in range (0, pop_size):
        fitness.append(evaluation.fitness(population[i], hotel, guests, max_days))
    print("generation", gen, ": best fitness", max(fitness), "\taverage fitness", sum(fitness)/len(fitness))

    max_fitnesses = []
    avg_fitnesses = []
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
                off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]], hotel, guests)
            else:
                off1 = population[parents_index[i]].copy()
                off2 = population[parents_index[i+1]].copy()

            # mutation
            if random.random() < mut_rate:
                off1 = mutation.permutation_swap(off1,hotel,guests)
            if random.random() < mut_rate:
                off2 = mutation.permutation_swap(off2,hotel,guests)
        
            offspring.append(off1)
            offspring_fitness.append(evaluation.fitness(off1, hotel, guests, max_days))
            offspring.append(off2)
            offspring_fitness.append(evaluation.fitness(off2, hotel, guests, max_days))
            i+=2  # update the counter

        # organize the population of next generation
        population, fitness = survivor_selection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
        #population, fitness = survivor_selection.replacement(population, fitness, offspring, offspring_fitness)
        
        gen += 1  # update the generation counter
        print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))
        max_fitnesses.append(max(fitness))
        avg_fitnesses.append(sum(fitness)/len(fitness))
    # evolution ends
    # print the final best solution(s)
    k = 0
    for i in range (0, pop_size):
        if fitness[i] == max(fitness):
            print("best solution", k, population[i], fitness[i])
            k += 1

    #visualize results
    visualization(max_fitnesses,avg_fitnesses,guests)

main()