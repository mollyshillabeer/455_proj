import random
from Guest import Guest
from Hotel import HotelRoom

#TODO: make sure solution is valid: number of guests can't exceed room size
# could attempt random mutations until one works
# or take advantage of structure, since rooms are ordered by capacity, can easily find 
#the index at which guests can fit within the rooms below it

"""
                R0    R1
Takes a list [[1,2],[3,4]....R13] numbers are guests ane each sublist is a room 
               ^
1 is the firt guest index to get into the room and 2 is the second index to get into the room
order the hotels by size (should be already ordered by index ex: [0,1,2,3])
also pass hotel object and guest object 
start by doing some mapping on what is a valid swap, 
hotel[0].size
guest[0].size 
def permutation_swap (individual):
    
     
    mutant = individual.copy()
    
    val1 = random.choice(mutant)
    val2 = random.choice(mutant)
    val1Position = mutant.index(val1)
    val2Position = mutant.index(val2)
    mutant[val1Position] = val2
    mutant[val2Position] = val1
    
    return mutant
"""

def permutation_swap (individual, hotel ,guest):
    for i in range(0,len(individual)):

        print("index of room is ",i)
        print("first guest index is", individual[i][0])
        print("first guest index is", individual[i][1])
        print(" ")
    


    print ("size of hotel is ", hotel[0].size)
    print ("size of guest is ",guest[0].size)
    if guest[0].size <= hotel[0].size:
        print("match")

    #mutant = individual.copy()
    #val1 = random.choice(mutant[0])
    #val2 = random.choice(mutant[1])
    #print(val1)
    #print(val2)
    #if statment to see if it can be valid
    #val1Position = mutant.index(val1)
    #val2Position = mutant.index(val2)
    #mutant[val1Position] = val2
    #mutant[val2Position] = val1 
    #return mutant

hotel = []
hotel.append(HotelRoom(7,1000,40))
guest = []
guest.append(Guest(3,5))
permutation_swap ([[1,2],[3,4]],hotel,guest)
