import math 

X_INCREMENT = .014474
Y_INCREMENT = .016761
# Author: Wayne Dyck
def haversine(origin, destination):
    lat1, long1 = origin
    lat2, long2 = destination
    radius = 3959 # of earth, in miles
 
    delta_lat = math.radians(lat2-lat1)
    delta_long = math.radians(long2-long1)
    a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(delta_long/2) * math.sin(delta_long/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    dist = round(radius * c, 2)
 
    return dist


def generate_coords(origin, radius, density=1):
    coords = []
    coords.append(origin)
    a, b = origin
    xmin, ymax = ((a + (X_INCREMENT * radius)), ((b - (Y_INCREMENT * radius))))
    xmax, ymin = ((a - (X_INCREMENT * radius)), ((b + (Y_INCREMENT * radius))))


generate_coords((30.274294, -97.740504), 2)