import json

from dataclasses import dataclass
from urllib.request import urlopen


url_for_get_coordinates = 'http://ip-api.com/json/{}'


@dataclass
class Coordinates:
    latitude: float
    longitude: float
    city: str

def get_coordinates_by_ip(ip: str) -> Coordinates:
    response_with_coordinates= _get_coordinates(ip)
    result = _parse_response_with_coordinates(response_with_coordinates)
    return Coordinates(
            latitude=result['lat'], 
            longitude=result['lon'], 
            city=result['city'])

def _get_coordinates(ip: str) -> str:
    return urlopen(url_for_get_coordinates.format(ip)).read()

def _parse_response_with_coordinates(
        response_with_coordinates: str) -> dict:
    full_json = json.loads(response_with_coordinates)
    result = {
            k: v for k, v in full_json.items() if k in ('lat', 'lon', 'city')}
    return result          


if __name__ == '__main__':
    print(get_coordinates_by_ip('178.121.23.27'))

