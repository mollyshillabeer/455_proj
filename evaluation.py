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
                currGuest=guests[individual[i][j]]
                num_days+=currGuest.num_days
                
                #room can't book any more guests in desired time frame, so stop calculating
                if num_days > max_days:
                    break
                
                #if a guest group can't fit in the room, they can't be booked, so no profit
                #also if the guest requires an accessible room or a smoke free room
                #profit is calculated as cost per night*number of nights
                #then subtract from the fitness if the guest has a bad rating,because they are more likely to trash the room
                if currGuest.size <= currRoom.size and ((currGuest.accessible and currRoom.accessible) or not currGuest.accessible) \
                    and ((currGuest.smoke_free and currRoom.smoke_free) or not currGuest.smoke_free):
                    fitness+=(currRoom.base_cost+currRoom.cost_per_person*currGuest.size)*currGuest.num_days
                    if currGuest.rating < 4:
                        fitness -= (50-currGuest.rating*10)
    return fitness