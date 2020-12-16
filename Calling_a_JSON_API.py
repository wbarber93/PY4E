# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py
# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse 
# that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely 
# identifies a place as within Google Maps.
  
import urllib.error, urllib.request, urllib.parse
import json

target = 'http://py4e-data.dr-chuck.net/json?' 
local = input('Enter location: ')
url = target + urllib.parse.urlencode({'address': local, 'key' : 42})

print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data)
print(json.dumps(js, indent = 4)) 
print('Place id', js['results'][0]['place_id'])
