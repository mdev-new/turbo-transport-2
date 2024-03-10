import math
from math import sin, cos, sqrt, atan2

import requests

# Thanks unknown student for making this key static :)))))))
# :)))))))))))))))))))))))))))))))))))))))))))))))))))))))))
DPMP_APIKEY = "3e86570d-56a1-4ec1-8012-c1a9f98d18cc"
DEG_TO_RAD = math.pi / 180
EARTH_RADIUS = 6371  # km


def get_dpmp(thing):
    req = requests.request(
        "POST",
        f'https://online.dpmp.cz/api/{thing}',
        json=('{"key":"' + DPMP_APIKEY + '"}')
    )

    return req


def get_overpass(url):
    return requests.get(url).json()


def haversine(point_a, point_b):
    # These get converted to radians directly in the calculations.
    lat1, lon1 = point_a
    lat2, lon2 = point_b

    d_lat = (lat2 - lat1) * DEG_TO_RAD
    d_lon = (lon2 - lon1) * DEG_TO_RAD

    # square of half the chord length between the points
    a = (sin(d_lat / 2) ** 2) + (sin(d_lon / 2) ** 2) * cos(lat1 * DEG_TO_RAD) * cos(lat2 * DEG_TO_RAD)

    # angular distance in radians
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return EARTH_RADIUS * c


def overlapping_pairs(arr):
    for i in range(1, len(arr)):
        yield [arr[i - 1], arr[i]]
