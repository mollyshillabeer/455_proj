#imports
from itertools import permutations
import random
import pandas as pd
import numpy as np
from Hotel import HotelRoom
from Guest import GuestGroup

def make_hotel():
    '''
    Make the hotel as a list of hotel rooms. Using information from Athina Luxury Suites
    in Greece. 14 rooms in total:
        -junior suite: 1 queen, 2 people. - 3 available. balcony. $880/night
        -master loft suite: double and sofa bed, 3 people. balcony. $880/night
        -junior cave suite: 1 king, 2 people. balcony. $953/night
        -deluxe suite: 1 king, 2 sofa bed, 4 people. balcony. $1246/night
        -petit cave suite: 1 king, 2 people. outdoor jacuzzi. $1392/night
        -honeymoon suite: 1 king, 2 people. jacuzzi & balcony. $1686/night
        -cave honeymoon suite: 1 king, 2 people. jacuzzi & balcony. $1760/night
        -black rock honeymoon suite: 1 king, 2 people. jacuzzi & balcony. $1906/night
        -cave suite: 1 king, 1 sofa bed, 4 people. jacuzzi & balcony. $1686/night
        -superior suite: 1 king, 2 people. jacuzzi & balcony. $1686/night
        -grand cave suite: 1 king, 1 sofa bed, 4 people. indoor and outdoor jacuzzi. $2126/night
        -royal suite: 2 kings, 1 sofa bed, 6 people. jacuzzi & balcony. $2492/night
    '''
    rooms=[]
    for i in range(3):
        rooms.append(HotelRoom(2,880,40))
    rooms.append(HotelRoom(2,953,40))
    rooms.append(HotelRoom(2,1392,40))
    rooms.append(HotelRoom(2,1686,40))
    rooms.append(HotelRoom(2,1686,40))
    rooms.append(HotelRoom(2,1760,40))
    rooms.append(HotelRoom(2,1906,40))
    rooms.append(HotelRoom(3,880,40))
    rooms.append(HotelRoom(4,1246,40))
    rooms.append(HotelRoom(4,1686,40))
    rooms.append(HotelRoom(4,2126,40))
    rooms.append(HotelRoom(6,2492,40))
    return rooms

def make_guest_file():
    '''
    Full set of possible guests from a kaggle dataset showing hotel reservations.
    Only a subset of size 1000 are used in the EA because this has upwards of 36,000 samples.
    Results are placed in guests.csv, should read from that for initialization.
    https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset
    '''
    df=pd.read_csv('HotelReservations.csv')
    df1=df[['no_of_adults','no_of_children','no_of_weekend_nights','no_of_week_nights']]
    #make aggregate features for total number of guests and total nights
    df1.insert(0,'num_guests',df1.loc[:,['no_of_adults','no_of_children']].sum(axis=1))
    df1.insert(0,'duration',df1.loc[:,['no_of_weekend_nights','no_of_week_nights']].sum(axis=1))
    #drop samples with size larger than the max size at Athina suites
    df1 = df1.drop(df1[df1.num_guests > 6].index)
    df1 = df1.drop(df1[df1.duration == 0].index)
    guests = df1.sample(n=1000,random_state=0)
    guests.to_csv('guests.csv',index=False)

def make_guests(num_guests):
    '''Returns a list of guest objects, number of which is specified in main.'''
    df=pd.read_csv('guests.csv')
    guests = []
    for i in range(num_guests):
        curr_row=df.iloc[i]
        guests.append(GuestGroup(curr_row.num_guests,curr_row.duration))
    return guests

#TODO: could do a second version that allows for conflicts in room sizes
def permutation(pop_size, num_guests, num_guests_per_room):
    """initialize a population of permutation. Using a heuristic to make sure there are no
    room size/guest size conflicts to start."""
    population = []
    backups=[]
    hotel = make_hotel()
    guests = make_guests(num_guests)
    num_rooms = len(hotel)
    #for each individual in population, create an initial solution
    for i in range(pop_size):
        indiv=[]
        backup=[] #guests that could be assigned in future but currently aren't
        guests_dict = {k: v for k,v in enumerate(guests)}
        #for each room in the hotel, pick from the subset of guests that can fit into the room
        #TODO: should randomly pick room
        for j in range(num_rooms):
            possible_guests = [a for a in guests_dict if guests_dict[a].size<=hotel[j].size]
            num_options = len(possible_guests)
            
            #randomly pick from guests that can fit and remove selected guests from full list
            if num_options >= num_guests_per_room:
                selected_guests = random.sample(possible_guests,num_guests_per_room)
                for elem in selected_guests:
                    guests_dict.pop(elem)
            elif num_options != 0:
                selected_guests = possible_guests
                for elem in selected_guests:
                    guests_dict.pop(elem)
                selected_guests.extend([-1]*(num_guests_per_room-num_options))
            else:
                selected_guests=[-1]*num_guests_per_room

            indiv.append(selected_guests)
        backup.append([a for a in guests_dict])
        population.append(indiv)
    return population, backups, hotel, guests