# from library.utils.booking_tools import search_service, get_price, estimate_cart
from geopy.geocoders import Nominatim, ArcGIS
from geopy.extra.rate_limiter import RateLimiter
from geopy import distance


# geolocator = Nominatim(user_agent="lasoota")
geolocator = ArcGIS()

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

location1 = geocode("Prateek Grand City, Siddharth Vihar, Ghaziabad, 201014, India", timeout=10)

location2 = geocode("Electronic city Metro, Noida Sector 62, Noida, Uttar Pradesh, 201301, India", timeout=10)

dist = distance.distance((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).km

print(location2.address)
print(location2.latitude, location2.longitude)

print(f"Distance: {dist:.2f} km")



# data = search_service("fan repair")
# print(data)

service = {'service': 'Electrician', 
'results': [{'category': 'Fan Services',
 'items': [
    {'code': 'FAN_REPAIR', 'name': 'Fan Repair', 'unit': 'per fan',
     'description': 'Fixing fan noise, slow speed, wiring issues'}]}]}
     

# price = get_price(service['results'][0]['items'][0]['code'], 2)
# print(price)

# price_data = {'code': 'FAN_REPAIR', 'name': 'Fan Repair', 'unit': 'per fan', 'unit_price': 300, 'quantity': 2, 'total_price': 600}


# est = estimate_cart([price_data])

# print(est)