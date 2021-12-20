import requests
import json
x = requests.get('https://api.weather.gov/gridpoints/ABQ/31,80/forecast')
data = json.loads(x.text)
print("coordinates: ", data['geometry']['coordinates'])

for item in data['properties']['periods']:
    print("ID: ", item['number'])
    print("Day: ", item['name'])
    print("startTime: ", item['startTime'])
    print("endTime: ", item['endTime'])
    print("windSpeed: ", item['windSpeed'])
    print("temperature: ", item['temperature'])
    print("temperatureUnit: ", item['temperatureUnit'])
    print("\n")
