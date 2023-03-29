#reinforcement learning?
#brute force?
import initialization
import evaluation
from operator import attrgetter

#TODO: run from within main, take guests and hotel as params
def greedy():
    num_guests=28
    num_guests_per_room=2
    max_days=3000
    guests = initialization.make_guests(num_guests)
    hotel = initialization.make_hotel()
    solution = [None]*len(hotel)
    #fill in order of cost and number of people in the group
    hotel_dict = {k: v.base_cost for k,v in enumerate(hotel)}
    guests_dict = {k: v for k,v in enumerate(guests)}

    for i in range(len(hotel)):
        next_room = max(hotel_dict, key=lambda x: hotel_dict[x])
        hotel_dict.pop(next_room)

        possible_guests = [a for a in guests_dict if guests_dict[a].size<=hotel[next_room].size]
        selected_guests = sorted(possible_guests,key=lambda x: guests[x].size, reverse=True)
        
        if len(selected_guests) >= num_guests_per_room:
            selected_guests = selected_guests[:num_guests_per_room]
        
        for elem in selected_guests:
            guests_dict.pop(elem)
        
        selected_guests.extend([-1]*(num_guests_per_room-len(selected_guests)))
        solution[next_room]=selected_guests

    fitness = evaluation.fitness(solution,hotel,guests,max_days)
    return solution, fitness
    