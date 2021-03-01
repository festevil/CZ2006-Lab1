from geopy.geocoders import GoogleV3
import geopy.distance
import googlemaps
import pandas
import gmplot

class MapData:
    """Gives us the Map Data of the address specified from street and town"""
    def __init__(self,street, town):
        self.street = street
        self.town = town
    def __GeocodeCoor(self):
        """Geocodes address to latitude and longitiude. Used in plotpoint."""
        GoogleAPI ='AIzaSyAT5ls2tvRCs9x0p4aVd7984HNocfpAOXE'
        geolocator = GoogleV3(api_key=GoogleAPI)
        loc = geolocator.geocode(self.street + " " + self.town)
        return loc
    
    def plotpoint(self):
        """Returns a google map with the specified location from street and town."""
        location = self.__GeocodeCoor()
        gmap = gmplot.GoogleMapPlotter(location.latitude, location.longitude, 20)
        gmap.marker(location.latitude,location.longitude)

    