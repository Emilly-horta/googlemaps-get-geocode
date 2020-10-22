from requests import get
from os import getenv

_API_KEY = getenv('API_KEY')

def get_geocode(address: str) -> dict:
    try:
        address_ok = address.replace(' ', '+')
        request_params = {
            'address': address_ok,
            'key': _API_KEY
        }
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        response = get(url, params=request_params).json()
        geocode = response['results'][0]['geometry']['location']
        return geocode
    
    except IndexError:
        return {
            'error': 'API_KEY is not defined.' 
        } 
