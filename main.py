from flask import Flask, render_template
from get_iss import iss_loc
from get_weather import get_wthr
from get_address import get_addr
from get_distance import get_dist
from get_country import get_cntry


app = Flask('app')

@app.route('/')
def iss_data():
  # Getting latitude and longitude of ISS location.
  iss_data = iss_loc()
  #print(iss_data)
  lat=iss_data[0]
  lon=iss_data[1]
  #print(lat,lon)
  
  
  # Getting weather below ISS on earth's surface.
  weather = get_wthr(lat, lon)
  #print(weather)
  # Getting temperature and description of weather.
  temp_c = round(weather['main']['temp'] - 273.15,2)
  desc = weather['weather'][0]['description']
  humd = weather['main']['humidity']
  #print(temp_c, desc)
  
  
  # Getting the address of ISS on earth surface
  address = get_addr(lat, lon)
  #print(address)
  cntry_code = address['results'][0]['locations'][0]['adminArea1']
  #print(cntry_code)
  
  if cntry_code == 'XZ':
    cntry_name = 'ISS is over ocean'
    #print(cntry_code)
    cntry_flg = "/static/images/B.jpg"
    cntry_cap = 'Not Applicable'
    cntry_pop = 'Not Applicable'
  else:
    cntry_code = address['results'][0]['locations'][0]['adminArea1']
    cntry_dtls = get_cntry(cntry_code)
    cntry_name = cntry_dtls[0]['name']['common']
    cntry_flg = cntry_dtls[0]['flags']['png']
    cntry_cap = cntry_dtls[0]['capital']
    cntry_pop = cntry_dtls[0]['population']
    #print(cntry_name, cntry_flg)
  cntry = cntry_name
  flg = cntry_flg
  captl = cntry_cap
  popln = cntry_pop
    
  
  
  # distance from the ISS to my location
  # My Location: Sudbury (lat: 46.5830385, lon: -81.6395742)
  distance = get_dist(lat, lon, 46.5830385, -81.6395742)
  dist = round(distance,2)
  #print(round(distance,2))
  
  return render_template('index.html', dist=dist, lat=lat, lon=lon, cntry=cntry, flg=flg, captl=captl, popln=popln, temp_c=temp_c, desc=desc, humd=humd)

app.run(host='0.0.0.0', port=8080)
