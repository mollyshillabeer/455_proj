def fitness_8queen (individual): 
    """Compute fitness of an invidual solution (maximization)"""    

    fitness = 0
    for room in individual:
        if room != -1:
            #TODO: added cost per person, ocean view, etc
            fitness+=room.cost
    
    return fitness