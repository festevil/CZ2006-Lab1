import MapData
import HDB_Flat
import numpy as np
import pandas as pd

class SearchManager:
    def __init__(self):
        HDBlist=[]
    def QueryData(pricelower,pricehigher, town, flattype,flatmodel,storeyrange,remaininglease):
        flatinfo=pd.read_csv("resale-flat-prices-2017.csv")
        if (pricelower>0):
            if (pricehigher==0):
                flatinfo=flatinfo[(flatinfo["resale_price"]>=pricelower)]
            elif (pricehigher<pricelower):
                #display error
                print("Error!")
            else:
                flatinfo=flatinfo[(pricehigher>=flatinfo["resale_price"]>=pricelower)]
        else:
            if (pricehigher>0):
                flatinfo=flatinfo[(flatinfo["resale_price"]<=pricehigher)]
        if (town!="ANY"):
            flatinfo=flatinfo[(flatinfo["town"]==town)]
        if (flattype!="ANY"):
            flatinfo=flatinfo[(flatinfo["flat_type"]==flattype)]
        if (flatmodel!="ANY"):
            flatinfo=flatinfo[(flatinfo["flat_model"]==flatmodel)]
        if (storeyrange!="ANY"):
            flatinfo=flatinfo[(flatinfo["storey_range"]==storeyrange)]
        if (remaininglease>0):
            flatinfo=flatinfo[(flatinfo["remaining_lease"]>remaininglease)]
        for index, row in flatinfo.iterrows():
            HDBlist.append(HDB_Flat(row["town"],row["flat_type"],row["street_name"],row["block"],row["storey_range"],row["floor_area_sqm"],row["flat_model"],row["remaining_lease"],row["resale_price"])
        
    def clearHDB():
        HDBlist.clear()
    def ShowMap(street, town):
        newmap = MapData(street, town)
        newmap.plotpoint()