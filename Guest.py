class Guest:
    #TODO: accessibility, ocean view, etc.
    def __init__(self,size,num_days):
        self.size=size
        self.num_days=num_days
        
    def getSize(self):
        return self.size

    def getNumDays(self):
        return self.num_days