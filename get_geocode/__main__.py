from get_geocode import get_geocode
from json import dumps

address = input('Address name: ')
print('Getting data...')

geocode = get_geocode(address)

print()
print(dumps(geocode, indent=4, sort_keys=True))