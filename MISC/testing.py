import requests
import datetime
import json
from time import sleep

while True:
    url = "https://discordapp.com/api/webhooks/1062344746183434300/u1RVXuwV2ltmYxHbbi8Z1tox3NC1pL6Bu8Nj77L5osufyrxjkm30H4mxXri0ucZIzQHq"
    data = {'content': f"active - {datetime.datetime.now()}"}
    r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    sleep(60)