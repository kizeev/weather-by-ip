from dataclasses import dataclass
from datetime import datetime
from urllib.request import urlopen

from coordinates import Coordinates


weather_api = 'https://api.openweathermap.org/data/3.0/onecall?
    lat={lat}&lon={lon}&exclude={part}
    &appid=129d2a91cccd61f6bbea5f5f7fd28410'


@dataclass
class WeatherType:
    pass


@dataclass
class Weather:
    temperature: int
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    response_with_weather = _get_weather(coordinates)
    return response_with_weather


def _get_weather(coordinates: Coordinates) -> Weather:
    url = weather_api.format(
            lat=coordinates.latitude, 
            lon=coordinates.longitude,
            part='')
    weather = urlopen(url).read()
    return weather



if __name__ == '__main__':
    print(get_weather(
        Coordinates(latitude=52.4313, longitude=30.9937, city='Gomel')))
