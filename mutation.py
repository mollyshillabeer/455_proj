import random
from Guest import GuestGroup
from Hotel import HotelRoom

def permutation_swap (individual,rooms,guests):
    
    match = False
    mutant = individual.copy()
    tries = 0

    while match != True and tries <= 10:
        randomRoom = random.choice(rooms)
        roomIndex = rooms.index(randomRoom)
        guestIndex = random.randint(0,len(mutant[roomIndex])-1)
        if guests[guestIndex].size <= rooms[roomIndex].size:
            randomRoomToSwitch = random.randint(0,len(individual)-1)
            randomGuestToSwitch = random.randint(0,len(individual[randomRoomToSwitch])-1)
            temp = mutant[roomIndex][guestIndex] 
            mutant[roomIndex][guestIndex] = mutant[randomRoomToSwitch][randomGuestToSwitch]
            mutant[randomRoomToSwitch][randomGuestToSwitch] = temp
            match = True     
        else:
            tries +=1
            match = False
    return mutant
