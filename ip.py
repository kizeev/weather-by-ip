import json
from urllib.request import urlopen


url_for_get_ip = 'https://api.myip.com'

def get_ip() -> str:
    ip_response = _get_ip_response(url_for_get_ip)
    ip = _parse_ip_response(ip_response)
    return ip

def _get_ip_response(url: str) -> str:
    return urlopen(url).read()


def _parse_ip_response(ip_response: str) -> str:
    return json.loads(ip_response)['ip']


if __name__ == '__main__':
    print(get_ip())
