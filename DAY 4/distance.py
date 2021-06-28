from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
Radius = 6373.0

lat1 = radians(.2921)
lon1 = radians(36.8219)
lat2 = radians(30.0444)
lon2 = radians(31.2357)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = Radius * c

print("Result:", str(distance) +"km")
