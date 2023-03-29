import random
from Guest import Guest
from Hotel import HotelRoom

def permutation_swap (individual,rooms,guests):
    
    match = False
    mutant = individual.copy()
    tries = 0

    while match != True and tries != 10:
        randomRoom = random.choice(rooms)
        randomGuest = random.choice(guests) 
        guestIndex = guests.index(randomGuest)
        roomIndex = rooms.index(randomRoom) 
        if guests[guestIndex].size <= rooms[roomIndex].size:
            randomGuestToSwitch = random.randint(0,len(individual)-1)
            mutant[roomIndex][randomGuestToSwitch] = guestIndex
            match = True     
        else:
            tries +=1
            match = False
    return mutant
