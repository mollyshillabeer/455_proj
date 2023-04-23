class GuestGroup:
    #TODO: accessibility, ocean view, etc.
    '''Guest object, representing 1 group that wants to stay in the hotel. most important features are 
    number of people in the group (size) and number of days they want to stay for (num_days)'''
    def __init__(self,size,num_days,pets=0,accesible=False,smoke_free=False):
        self.size=size
        self.num_days=num_days
        self.pets=pets
        self.accessible=accesible
        self.smoke_free=smoke_free