#reinforcement learning?
#brute force?
import initialization
import evaluation
from operator import attrgetter

#TODO: run from within main, take guests and hotel as params
def greedy():
    '''
    Greedy approach to solving this problem. Fills the most expensive rooms first, with the largest groups possible.
    This should mimic how humans would schedule something for profit maximization.
    '''
    num_guests=70
    num_guests_per_room=5
    max_days=3000
    guests = initialization.make_guests(num_guests)
    hotel = initialization.make_hotel()
    solution = [None]*len(hotel)
    hotel_dict = {k: v.base_cost for k,v in enumerate(hotel)}
    guests_dict = {k: v for k,v in enumerate(guests)}

    #for each room in the hotel, fill with guests from the list of possible guests
    for i in range(len(hotel)):
        next_room = max(hotel_dict, key=lambda x: hotel_dict[x])
        hotel_dict.pop(next_room)

        #select from guests of a group size equal to or less than the capacity of the room, pick the largest ones
        possible_guests = [a for a in guests_dict if guests_dict[a].size<=hotel[next_room].size]
        selected_guests = sorted(possible_guests,key=lambda x: guests[x].size, reverse=True)
        
        #pick the correct number of guests
        if len(selected_guests) >= num_guests_per_room:
            selected_guests = selected_guests[:num_guests_per_room]
        
        #remove selected guests from the list of candidates
        for elem in selected_guests:
            guests_dict.pop(elem)
        
        #add room to the soluion, unfilled spots get a -1
        selected_guests.extend([-1]*(num_guests_per_room-len(selected_guests)))
        solution[next_room]=selected_guests

    fitness = evaluation.fitness(solution,hotel,guests,max_days)
    return solution, fitness