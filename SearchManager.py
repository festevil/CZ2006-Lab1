import MapData
import numpy as np
import pandas as pd

class SearchManager:
    def QueryData(pricelower,pricehigher, town, flattype,flatmodel,storeyrange,remaininglease):
        flatinfo=pd.read_csv("resale-flat-prices-2017.csv")
        if(pricelower>0):
            if(pricehigher<pricelower):
                "display error"
        
    def ShowMap(street, town):
        newmap = MapData(street, town)
        newmap.plotpoint()