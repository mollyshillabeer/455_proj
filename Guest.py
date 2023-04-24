class GuestGroup:
    '''Guest object, representing 1 group that wants to stay in the hotel. most important features are 
    number of people in the group (size) and number of days they want to stay for (num_days)'''
    def __init__(self,size,num_days,accessible=False,smoke_free=False,rating=5):
        self.size=size
        self.num_days=num_days
        self.rating = rating
        self.accessible=accessible
        self.smoke_free=smoke_free