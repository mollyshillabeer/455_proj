def fitness(individual,rooms,guests,max_days): 
    """Compute fitness of an invidual solution (maximization)"""    

    fitness = 0
    #iterate over each room in solution
    for i in range(len(individual)):
        currRoom=rooms[i]
        num_days=0
        #iterate over each guest in each room
        for j in range(len(individual[i])):
            #if there's a guest staying in the room, calculate how much they pay for it
            if individual[i][j] != -1:
                #TODO: accessibility, ocean view, etc
                currGuest=guests[individual[i][j]]
                num_days+=currGuest.num_days
                
                #room can't book any more guests in desired time frame, so stop calculating
                if num_days > max_days:
                    break
                
                #if a guest group can't fit in the room, they can't be booked, so no profit
                #profit is calculated as cost per night*number of nights
                if currGuest.size <= currRoom.size:
                    fitness+=(currRoom.base_cost+currRoom.cost_per_person*currGuest.size)*currGuest.num_days
    return fitness