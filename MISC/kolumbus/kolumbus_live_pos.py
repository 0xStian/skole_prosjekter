import requests, json, re
from geopy.geocoders import Nominatim # get adress from coords
import pandas as pd
import plotly.express as px

geolocator = Nominatim(user_agent="geoapi")
realtime_bus_api = "https://api.kolumbus.no/api/vehicles/realtimehub"
headers = {"Content-Type": "application/json"}

dot_size = 3


def get_bus_data():
    response = requests.get(realtime_bus_api, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else: get_bus_data()

def normalise_string(text):
    return str(text).replace('å','aa').replace('ø','o').replace('æ', 'ae')

info = ["size,latitude,longitude,destination"]
def save_bus_data(bus_data):
    with open("livepos.txt", "w") as f: pass
    for bus in bus_data:
        vehicle_id = bus['vehicle_id']
        line_name = bus['line_name']
        bus_coordinates = f"{bus['latitude']:.9f},{bus['longitude']:.9f}"
        lat = float(bus['latitude'])
        lon = float(bus['longitude'])
        speed = f"{int(bus['speed'])} km/h"
        destination= str(normalise_string(bus["destination_display"]))
        start_position = bus["origin_name"]
        info.append(f"{dot_size},{lat},{lon},{destination}")
    for line in info:
        line = normalise_string(line.lower()).title()
        with open("livepos.txt", "a") as f:
            f.writelines(f"{line}\n")


def show_image():   
    df = pd.read_csv("livepos.txt")
    fig = px.scatter_mapbox(df,lat="Latitude",lon="Longitude",hover_name="Destination",size="Size", zoom=12, color_discrete_sequence=["blue"])
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout()
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()


data = get_bus_data()
save_bus_data(data)
show_image()