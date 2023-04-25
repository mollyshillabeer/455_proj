import random
from Guest import GuestGroup
from Hotel import HotelRoom

def permutation_swap (individual,rooms,guests):
    '''
    swap 2 guests in 1 candidate solution if it wouldn't break the constraint of 
    fitting into the hotel room. try 10 times before giving up.
    '''
    match = False
    mutant = individual.copy()
    tries = 0
    # Ensures that the algorithm attepts to create the mutation up to 10 times
    while match != True and tries <= 10:
        # Picks a random room and gets its index
        randomRoom = random.choice(rooms)
        roomIndex = rooms.index(randomRoom)
        # Picks a random guest and gets its index
        guestIndex = random.randint(0,len(mutant[roomIndex])-1)
        guestId = mutant[roomIndex][guestIndex]
        
        #second chosen guest
        randomRoomToSwitch = random.randint(0,len(individual)-1)
        randomGuestToSwitch = random.randint(0,len(individual[randomRoomToSwitch])-1)
        guest2Id = mutant[randomRoomToSwitch][randomGuestToSwitch]
        
        # Checks if the number of guests part of the guest's group can fit in the random room
        if guests[guestId].size <= rooms[randomRoomToSwitch].size and guests[guest2Id].size <= rooms[roomIndex].size :
            temp = mutant[roomIndex][guestIndex] 
            mutant[roomIndex][guestIndex] = mutant[randomRoomToSwitch][randomGuestToSwitch]
            mutant[randomRoomToSwitch][randomGuestToSwitch] = temp
            match = True     
        else:
            tries +=1
            match = False
    return mutant
