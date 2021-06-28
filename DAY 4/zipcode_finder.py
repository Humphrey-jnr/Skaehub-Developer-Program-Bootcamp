from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")

zipcode1 = "21345"
print("\nZipcode:",zipcode1)
location = geolocator.geocode(zipcode1)
print("Details of the szip code location:")
print(location.address) 
