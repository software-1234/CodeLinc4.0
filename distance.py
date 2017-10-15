import database
import googlemaps
import decimal
import math

def get_distance(latlng, filter):	
    D = decimal.Decimal
    res = []
    if filter == "all":
        res = database.get_valid_locations_non_json()
    else:
        res = database.get_valid_locations_by_type(filter)
    #gmaps = googlemaps.Client(key='AIzaSyApuvnawK-aqRhvTW9tsLoKJGT-24fPrvY')

    lat2 = latlng[0]
    lon2 = latlng[1]

    R = 6373.0
    min_row = None
    min_distance = 0
    for r in res:
        lat1 = math.radians(D(r[17]))
        lon1 = math.radians(D(r[18]))
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        if distance > min_distance:
            print(distance)
            min_distance = distance
            min_row = r
        
    return (min_distance,min_row)
      
	
