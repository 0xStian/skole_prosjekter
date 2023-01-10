import requests, json, time, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt         

# "dataset.txt", sep=":", names=["latitude", "longitude"]"
realtime_bus_api = "https://api.kolumbus.no/api/vehicles/realtimehub"
headers = {"Content-Type": "application/json"}



def get_bus_data():
    response = requests.get(realtime_bus_api, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        get_bus_data()

def append_to_file(cords):
    with open("dataset.txt", "a") as f:
        f.writelines(f"{cords}\n")

def save_bus_data(bus_data):
    for bus in bus_data:
        line_name = bus['line_name']
        destination= bus["destination_display"]
        bus_coordinates = f"{bus['latitude']:.9f}, {bus['longitude']:.9f}"
        try: next_platform_coordinates = f"{bus['next_platform']['latitude']:.9f}, {bus['next_platform']['longitude']:.9f}"
        except: next_platform_coordinates = "Not Found"
        if destination == "Stavanger" and line_name == "8":
            append_to_file(f"{bus['latitude']:.9f},{bus['longitude']:.9f}")
            
            
        
while True:
    data = get_bus_data()
    save_bus_data(data)
    time.sleep(2)