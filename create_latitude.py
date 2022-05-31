import random
import math
import pandas as pd
from math import *

def generate_random_gps(base_log=None, base_lat=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    loga = '%.6f' % longitude
    lata = '%.6f' % latitude
    return float(loga), float(lata)




EARTH_RADIUS = 6371  
EARTH_CIRCLE = 2 * math.pi * EARTH_RADIUS

def get_distance(log1, log2, lat1, lat2):
    t1 = abs(log1-log2) * EARTH_CIRCLE / 360
    t2 = abs(lat1-lat2) * EARTH_CIRCLE / 360
    distance = (t1**2+t2**2)**0.5*1000
    return distance

def get_tuple_distance(n1,n2):
    return get_distance(n1[1],n2[1],n1[2],n2[2])

def get_log_distance(n1,n2):
    return abs(n1[1]-n2[1]) * EARTH_CIRCLE / 360

def get_lat_distance(n1,n2):
    return abs(n1[2]-n2[2]) * EARTH_CIRCLE / 360



def get_data(path = "data.csv"):
    import pandas as pd

    data = pd.read_csv("data.csv")

    data = data.values

    res = []

    for i in data:
        
        t = (int(i[0]),i[1],i[2])
        res.append(t)
    return res


# log1, lat1 = generate_random_gps(base_log=120.7, base_lat=30, radius=200)
# log2, lat2 = generate_random_gps(base_log=120.7, base_lat=30, radius=200)
# print(log1,lat1)

# print(get_distance(log1, log2, lat1, lat2))

if __name__ == "__main__":

    N = 50
    lo = []
    la = []

    for i in range(N):
        lot,lat = generate_random_gps(base_log=120.7, base_lat=30, radius=500)
        lo.append(lot)
        la.append(lat)

    pdcsv = pd.DataFrame({
        "index":list(range(N)),
        "longitude":lo,
        "latitude":la
    })

    pdcsv.to_csv("data.csv",index=0)






