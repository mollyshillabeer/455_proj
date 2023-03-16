import random


def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""
    population = []
    fitness = []

    #pool all of current population and offspring
    mu = len(current_pop)
    curr = list(zip(current_fitness,current_pop))
    off = list(zip(offspring_fitness,offspring))
    full_pop = curr+off
    #rank full population, pick the top mu individuals for the new population
    full_pop.sort(key=lambda a: a[0], reverse=True)
    top_mu = full_pop[:mu]
    population = [a[1] for a in top_mu]
    fitness = [a[0] for a in top_mu]
    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    #rank individuals in current population
    lam = len(offspring)
    curr = list(zip(current_fitness,current_pop))
    curr.sort(key=lambda a: a[0])
    #pick mu-lambda best individuals from current population
    pop = curr[lam:]
    #replace lambda worst individuals from current pop with all of the offspring
    population = [a[1] for a in pop] + offspring
    fitness = [a[0] for a in pop] + offspring_fitness
    return population, fitness
