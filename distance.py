import database
import googlemaps
def getDistance():	
	my_latitudes=database.get_valid_locations()
	print(len(my_latitudes))
	gmaps = googlemaps.Client(key='AIzaSyApuvnawK-aqRhvTW9tsLoKJGT-24fPrvY')
      
	
