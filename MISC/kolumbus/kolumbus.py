import requests, json, time, os

realtime_bus_api = "https://api.kolumbus.no/api/vehicles/realtimehub"
headers = {"Content-Type": "application/json"}


def get_bus_data():
    response = requests.get(realtime_bus_api, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        get_bus_data()


def save_bus_data(bus_data):
    for bus in bus_data:
        is_active = bus['is_active']
        vehicle_id = bus['vehicle_id']
        line_name = bus['line_name']
        bus_coordinates = f"{bus['latitude']:.9f}, {bus['longitude']:.9f}"
        speed = f"{int(bus['speed'])} km/h"
        destination= bus["destination_display"]
        delay = bus["delay"]
        try: next_platform_name = bus["next_platform"]["name"]
        except: next_platform_name = bus["next_stop_name"]
        try: next_platform_coordinates = f"{bus['next_platform']['latitude']:.9f}, {bus['next_platform']['longitude']:.9f}"
        except: next_platform_coordinates = "Not Found"
        with open ("data.txt", "w") as f:
            f.write(f"\n[{line_name}]{destination}  |\tActive: {is_active}\n")
            f.write(f"="*60 + "\n")
            f.write(f"Speed: {speed}\n")
            f.write(f"Bus_Coordinates: {bus_coordinates}\n")
            f.write(f"."*60 + "\n")
            f.write(f"Next platform: {next_platform_name}\n")
            f.write(f"Platform_coordinates: {next_platform_coordinates}\n")
            f.write(f"="*60 + "\n")

while True:
    data = get_bus_data()
    save_bus_data(data)
