import os
import urllib.request
import json


def get_addr(lat, lon):
  
  mR_key = os.environ['maprequest']
  url = f'http://www.mapquestapi.com/geocoding/v1/reverse?key={mR_key}&location={lat},{lon}&includeRoadMetadata=true&includeNearestIntersection=true'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result