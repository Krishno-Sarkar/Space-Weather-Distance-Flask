import os
import urllib.request
import json
from get_iss import iss_loc

iss_data = iss_loc()

lat = iss_data[0]
lon = iss_data[1]

def get_wthr(lat, lon):
  API_key = os.environ['weather']
  url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result