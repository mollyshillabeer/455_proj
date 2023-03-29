import random
from Guest import Guest
from Hotel import HotelRoom

def permutation_swap (individual,rooms,guests):
    match = False
    mutant = individual.copy()
    while match != True:
        randomRoom = random.choice(rooms)
        randomGuest = random.choice(guests) 
        guestIndex = guests.index(randomGuest)
        roomIndex = rooms.index(randomRoom) 
        if guests[guestIndex].size <= rooms[roomIndex].size:
            randomGuestToSwitch = random.randint(0,1)
            mutant[roomIndex][randomGuestToSwitch] = guestIndex
            match = True     
        else:
            match = False
    return mutant
