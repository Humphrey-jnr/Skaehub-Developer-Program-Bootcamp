from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

def city(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return city, state, country
print(city("1.2921, 36.8219"))