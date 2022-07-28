import urllib.request
import json


def get_cntry(name):
  url = f'https://restcountries.com/v3.1/alpha/{name}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result