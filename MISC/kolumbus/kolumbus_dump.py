import requests, json

realtime_bus_api = "https://api.kolumbus.no/api/vehicles/realtimehub"
headers = {"Content-Type": "application/json;v=1"}


def get_bus_data():
    response = requests.get(realtime_bus_api, headers=headers)
    data = json.loads(response.text)
    return data

def save_bus_data(data):
    with open("bus_data.json", "w") as f:
        json.dump(data, f, indent=4)
    
bus_data = get_bus_data()
save_bus_data(bus_data)

