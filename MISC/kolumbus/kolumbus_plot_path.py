import requests, json, time, os
from geopy.geocoders import Nominatim # get adress from coords

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
import plotly.express as px

geolocator = Nominatim(user_agent="geoapi")
realtime_bus_api = "https://api.kolumbus.no/api/vehicles/realtimehub"
headers = {"Content-Type": "application/json"}

def show_image():
    df = pd.read_csv("dataset.txt")
    # df = pd.read_csv("dataset_sandnes_hommersaak.txt")
    fig = px.scatter_mapbox(df,lat="latitude",lon="longitude",zoom=11, color_discrete_sequence=["blue"])
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

show_image()
