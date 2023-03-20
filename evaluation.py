def fitness(individual,rooms,guests): 
    """Compute fitness of an invidual solution (maximization)"""    

    fitness = 0
    for i in range(len(individual)):
        currRoom=rooms[i]
        for j in range(len(individual[i])):
            if individual[i][j] != -1:
                #TODO: accessibility, ocean view, etc
                #(cost+cost per person*num people)*duration
                currGuest=guests[individual[i][j]]
                fitness+=(currRoom.getCost()+currRoom.getPerPersonCost()*currGuest.getSize())*currGuest.getNumDays()
    return fitness