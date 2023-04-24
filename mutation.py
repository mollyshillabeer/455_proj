import random
from Guest import GuestGroup
from Hotel import HotelRoom

def permutation_swap (individual,rooms,guests):
    
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
        # Checks if the number of guests part of the guest's group can fit in the random room
        if guests[guestIndex].size <= rooms[roomIndex].size:
            # If they do fit then perform a switch with the guest in the room
            randomRoomToSwitch = random.randint(0,len(individual)-1)
            randomGuestToSwitch = random.randint(0,len(individual[randomRoomToSwitch])-1)
            # Compose the mutant of all the switched rooms
            temp = mutant[roomIndex][guestIndex] 
            mutant[roomIndex][guestIndex] = mutant[randomRoomToSwitch][randomGuestToSwitch]
            mutant[randomRoomToSwitch][randomGuestToSwitch] = temp
            match = True     
        else:
            tries +=1
            match = False
    return mutant
