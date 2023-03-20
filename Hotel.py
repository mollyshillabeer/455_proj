class HotelRoom:
    #TODO: accessibility, ocean view, etc.
    def __init__(self,size,base_cost,cost_per_person):
        self.size=size
        self.base_cost=base_cost
        self.cost_per_person=cost_per_person
        
    def getSize(self):
        return self.size

    def getCost(self):
        return self.base_cost
    
    def getPerPersonCost(self):
        return self.cost_per_person