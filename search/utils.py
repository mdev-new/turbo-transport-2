import math
from math import sin, cos, sqrt, atan2
from .constants import EARTH_RADIUS, DPMP_APIKEY, DEG_TO_RAD

import requests
from functools import cache

def get_dpmp(thing):
    req = requests.request(
        "POST",
        f'https://online.dpmp.cz/api/{thing}',
        json=('{"key":"' + DPMP_APIKEY + '"}')
    )

    return req.json()

@cache
def get_line_connections(line):
    return get_dpmp(f"currentConnections?line={line}")

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
