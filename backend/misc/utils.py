import math
from math import sin, cos, sqrt, atan2
from .constants import EARTH_RADIUS, DEG_TO_RAD

import requests


def get_overpass(url):
    return requests.get(url).json()


def haversine(lat1, lon1, lat2, lon2):
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
