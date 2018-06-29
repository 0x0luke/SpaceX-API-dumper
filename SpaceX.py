import json
import requests
import datetime

spacex_url = requests.get("https://api.spacexdata.com/v2/launches/latest")
jsondata = spacex_url.json()

json_dump = json.dumps(jsondata)

strjson = json.loads(json_dump)

print("Mission Name:",strjson['mission_name'])
print("Flight Number:",strjson['flight_number'])
print("Rocket Name:",strjson['rocket']['rocket_name'])
