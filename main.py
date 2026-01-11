from library.utils.booking_tools import search_service, get_price, estimate_cart


# data = search_service("fan repair")
# print(data)

service = {'service': 'Electrician', 
'results': [{'category': 'Fan Services',
 'items': [
    {'code': 'FAN_REPAIR', 'name': 'Fan Repair', 'unit': 'per fan',
     'description': 'Fixing fan noise, slow speed, wiring issues'}]}]}
     

# price = get_price(service['results'][0]['items'][0]['code'], 2)
# print(price)

price_data = {'code': 'FAN_REPAIR', 'name': 'Fan Repair', 'unit': 'per fan', 'unit_price': 300, 'quantity': 2, 'total_price': 600}


est = estimate_cart([price_data])

print(est)