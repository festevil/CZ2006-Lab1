class HDB_FLat:
    def __init__(self, town, flatType, streetName, block, storeyRange, floorArea, flatModel, remainingLease, resalePrice): # constructor
        self.town = town
        self.flatType = flatType
        self.streetName = streetName
        self.block = block
        self.storeyRange = storeyRange
        self.floorArea = floorArea
        self.flatModel = flatModel
        self.remainingLease = remainingLease
        self.resalePrice = resalePrice
		
    @classmethod
    def get_town(town):
        return self.town
        
    def get_flatType(flatType):
        return self.flatType
        
    def get_streetName(streetName):
        return self.streetName
        
    def get_storeyName(storeyRange):
        return self.storeyRange
        
    def get_floorArea(floorArea):
        return self.floorArea      
        
    def get_flatModel(flatModel):
        return self.flatModel
        
    def get_remainingLease(remainingLease):
        return self.remainingLease
        
    def get_resalePrice(resalePrice):
        return self.resalePrice
        
    #additional method (unsure need or not)
    def set_town(self, town):
        self.town = town
    def set_flatType(self, flatType):
        self.flatType = flatType
    def set_streetName(self, streetName):
        self.streetName = streetName
    def set_storeyRange(self, storeyRange):
        self.storeyRange = storeyRange
    def set_floorArea(self, floorArea):
        self.floorArea = floorArea
    def set_flatModel(self, flatModel):
        self.flatModel = flatModel
    def set_remainingLease(self, remainingLease):
        self.remainingLease = remainingLease
    def set_resalePrice(self, resalePrice):
        self.resalePrice = resalePrice
    
    
    
    
    
    