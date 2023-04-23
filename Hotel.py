class HotelRoom:
    # cost changes during season???
    '''Hotel room object. list of them make up a hotel. Most important features are capacity (size),
    cost per night (base_cost), and additional cost per person (cost_per_person)'''
    def __init__(self,size,base_cost,cost_per_person,pet_fee=0,accessible=False,smoke_free=False):
        self.size=size
        self.base_cost=base_cost
        self.cost_per_person=cost_per_person
        self.pet_fee=pet_fee
        self.accessible=accessible
        self.smoke_free=smoke_free
