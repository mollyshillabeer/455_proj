class HotelRoom:
    #TODO: accessibility, ocean view, etc.
    def __init__(self,size,base_cost,cost_per_person,pet_fee=0,accesible=False,ocean_view=False,smoke_free=False):
        self.size=size
        self.base_cost=base_cost
        self.cost_per_person=cost_per_person
        self.pet_fee=pet_fee
        self.accessible=accesible
        self.ocean_view=ocean_view
        self.smoke_free=smoke_free
