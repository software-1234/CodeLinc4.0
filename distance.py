import database
import googlemaps
def getDistance():	
	my_latitudes=database.get_valid_locations()
	print my_latitudes.length
	gmaps = googlemaps.Client(key='AIzaSyApuvnawK-aqRhvTW9tsLoKJGT-24fPrvY')
      
	
