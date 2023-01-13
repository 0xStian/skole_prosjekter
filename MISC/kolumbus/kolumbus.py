import requests, json, time, os
from geopy.geocoders import Nominatim # get adress from coords
geolocator = Nominatim(user_agent="geoapi")
realtime_bus_api = "https://api.kolumbus.no/api/vehicles/realtimehub"
headers = {"Content-Type": "application/json"}



def get_driving_direction(degrees):
    directions = ['North', 'North East', 'East', 'South East', 'South', 'South West', 'West', 'North West']
    ix = round(degrees / (360. / len(directions)))
    return str(directions[ix % len(directions)])
    
def normalise_string(text):
    return str(text).replace('å','aa').replace('ø','o').replace('æ', 'ae')

    
def get_bus_data():
    response = requests.get(realtime_bus_api, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        get_bus_data()


def save_bus_data(bus_data):
    for bus in bus_data:
        if bus["destination_display"] == "Sandnes via Riskafeltet-Maudland" and bus["line_name"] == "21":
            is_active = bus['is_active']
            vehicle_id = bus['vehicle_id']
            line_name = bus['line_name']
            bus_coordinates = f"{bus['latitude']:.9f},{bus['longitude']:.9f}"
            speed = f"{int(bus['speed'])} km/h"
            destination= normalise_string(bus["destination_display"])
            delay = bus["delay"]
            heading = get_driving_direction(int(bus["heading"]))
            start_position = normalise_string(bus["origin_name"])
            bus_geo_location = str(geolocator.reverse(bus_coordinates))
            bus_street_location = normalise_string(f"{bus_geo_location.split(',')[0]}, {bus_geo_location.split(',')[1]}")
            try: next_platform_name = normalise_string(bus["next_platform"]["name"])
            except: next_platform_name = normalise_string(bus["next_stop_name"])
            try: next_platform_coordinates = f"{bus['next_platform']['latitude']:.9f}, {bus['next_platform']['longitude']:.9f}"
            except: next_platform_coordinates = "Not Found"
            with open ("data.txt", "a") as f:
                f.write(f"\n{start_position} --> [{line_name}]{destination} |\tActive: {is_active}\n")
                f.write(f"="*80 + "\n")
                f.write(f"Speed:      \t\t\t{speed}\n")
                f.write(f"Current Location:\t\t{bus_street_location}\n")
                f.write(f"Bus Coordinates\t\t\t({bus_coordinates})\n")
                f.write(f"Heading:    \t\t\t{heading}\n")
                f.write(f"~"*80 + "\n")
                f.write(f"Next platform:   \t\t{next_platform_name}\n")
                f.write(f"Platform_coordinates:\t{next_platform_coordinates}\n")
                f.write(f"Delay:   \t\t\t\t{delay} min\n")
                f.write(f"="*80 + "\n")

while True:
    data = get_bus_data()
    save_bus_data(data)
