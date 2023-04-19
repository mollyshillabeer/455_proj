#imports
import random
import copy

#find what room a specified guest is staying in
def find_room(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return i, j
            
def permutation_cut_and_crossfill (p1, p2, rooms, guests):
    # Randomly Select a Guest
    selected_guest = random.randint(0, len(guests)-1)

    # Record Index of Selected Guest in Both Room Assignments
    room_index1, guest_index1 = find_room(p1, selected_guest)
    room_index2, guest_index2 = find_room(p2, selected_guest)
    
    # Copy Guest Room Assignments
    offspring1 = copy.deepcopy(p1)
    offspring2 = copy.deepcopy(p2)
    
    # Swap Guests in P1
    temp1 = offspring1[room_index1][guest_index1]
    offspring1[room_index1][guest_index1] = offspring1[room_index2][guest_index2]
    offspring1[room_index2][guest_index2] = temp1
    
    # Swap guests in P2
    temp2 = offspring2[room_index2][guest_index2]
    offspring2[room_index2][guest_index2] = offspring2[room_index1][guest_index1]
    offspring2[room_index1][guest_index1] = temp2
    
    # Invalid room combination found in offspring1, reset selection
    if rooms[room_index1].size < offspring1[room_index1][guest_index1].size or rooms[room_index2].size < offspring1[room_index2][guest_index2].size: 
        return p1, p2
    
    # Invalid room combination found in offspring2, reset selection
    if rooms[room_index1].size < offspring2[room_index1][guest_index1].size or rooms[room_index2].size < offspring2[room_index2][guest_index2].size:
        return p1, p2
    
    return offspring1, offspring2
