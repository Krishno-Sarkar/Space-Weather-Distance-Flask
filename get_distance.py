import geopy.distance

def get_dist(coord_1_lat, coord_1_lon, coord_2_lat, coord_2_lon):
  coord_1 = (coord_1_lat, coord_1_lon)
  coord_2 = (coord_2_lat, coord_2_lon)
  
  distance = geopy.distance.distance(coord_1,coord_2).km
  # https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

  return distance