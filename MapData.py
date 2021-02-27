from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps
import pandas
import gmplot

class MapData:
    def __init__(self,street, town):
        self.street = street
        self.town = town
    def __GeocodeCoor(self):
        GoogleAPI ='AIzaSyAT5ls2tvRCs9x0p4aVd7984HNocfpAOXE'
        geolocator = GoogleV3(api_key=GoogleAPI)
        loc = geolocator.geocode(self.street + " " + self.town)
        return loc
    
    def plotpoint(self):
        location = self.__GeocodeCoor()
        gmplot.GoogleMapPlotter(location.latitude, location.longitude, 20)
    