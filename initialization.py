#imports
from itertools import permutations
import random
import pandas as pd
import numpy as np
from Hotel import HotelRoom
from Guest import GuestGroup

#TODO: this needs serious modification to make valid permutations and include specific data
#use hotel and guest classes
def permutation (pop_size, chrom_length):
    """initialize a population of permutation"""

    population = []
    # student code begin
    # each individual is represented by a list of integers from 1 to 8
    chrom = list(range(1,chrom_length+1))
    #randomly select initial population from all possible solutions
    population = random.sample(list(permutations(chrom)),pop_size)
    population = [list(t) for t in population] #convert from tuple to list
    #student code end
    return population

def make_hotel():
    #all have ocean views, 14 rooms in total
    #junior suite: 1 queen, 2 people. - 3 available. balcony. $880/night
    #master loft suite: double and sofa bed, 3 people. balcony. $880/night
    #junior cave suite: 1 king, 2 people. balcony. $953/night
    #deluxe suite: 1 king, 2 sofa bed, 4 people. balcony. $1246/night
    #petit cave suite: 1 king, 2 people. outdoor jacuzzi. $1392/night
    #honeymoon suite: 1 king, 2 people. jacuzzi & balcony. $1686/night
    #cave honeymoon suite: 1 king, 2 people. jacuzzi & balcony. $1760/night
    #black rock honeymoon suite: 1 king, 2 people. jacuzzi & balcony. $1906/night
    #cave suite: 1 king, 1 sofa bed, 4 people. jacuzzi & balcony. $1686/night
    #superior suite: 1 king, 2 people. jacuzzi & balcony. $1686/night
    #grand cave suite: 1 king, 1 sofa bed, 4 people. indoor and outdoor jacuzzi. $2126/night
    #royal suite: 2 kings, 1 sofa bed, 6 people. jacuzzi & balcony. $2492/night
    rooms=[]
    for i in range(3):
        rooms.append(2,880,40)
    rooms.append(2,953,40)
    rooms.append(2,1392,40)
    rooms.append(2,1686,40)
    rooms.append(2,1686,40)
    rooms.append(2,1760,40)
    rooms.append(2,1906,40)
    rooms.append(3,880,40)
    rooms.append(4,1246,40)
    rooms.append(4,1686,40)
    rooms.append(4,2126,40)
    rooms.append(6,2492,40)
    return rooms
    

#subset of guests to use in the EA
#results are placed in guests.csv, should read from that for initialization
def make_guest_file():
    #https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset
    df=pd.read_csv('HotelReservations.csv')
    df1=df[['no_of_adults','no_of_children','no_of_weekend_nights','no_of_week_nights']]
    df1.insert(0,'num_guests',df1.loc[:,['no_of_adults','no_of_children']].sum(axis=1))
    df1.insert(0,'duration',df1.loc[:,['no_of_weekend_nights','no_of_week_nights']].sum(axis=1))
    df1 = df1.drop(df1[df1.num_guests > 6].index)
    df1 = df1.drop(df1[df1.duration == 0].index)
    guests = df1.sample(n=1000,random_state=0)
    guests.to_csv('guests.csv',index=False)
    
def make_guests(num_guests):
    #set num_guests to 70
    df=pd.read_csv('guests.csv')
    guests = []
    for i in range(num_guests):
        guests.append(GuestGroup(df.iloc[i]))
make_guests(70)