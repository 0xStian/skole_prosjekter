# import requests
# import datetime
# import json
# from time import sleep

# while True:
#     url = "https://discordapp.com/api/webhooks/1062344746183434300/u1RVXuwV2ltmYxHbbi8Z1tox3NC1pL6Bu8Nj77L5osufyrxjkm30H4mxXri0ucZIzQHq"
#     data = {'content': f"active - {datetime.datetime.now()}"}
#     r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
#     sleep(60)
from geopy.geocoders import Nominatim
Latitude = "25.594095"
Longitude = "85.137566"
 
 
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
 
location = geolocator.reverse(Latitude+","+Longitude)
 
# Display
print(location)