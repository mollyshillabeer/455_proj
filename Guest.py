class Guest:
    #TODO: accessibility, ocean view, etc.
    def __init__(self,size,num_days,pets=0,accesible=False,ocean_view=False,smoke_free=False):
        self.size=size
        self.num_days=num_days
        self.pets=pets
        self.accessible=accesible
        self.ocean_view=ocean_view
        self.smoke_free=smoke_free