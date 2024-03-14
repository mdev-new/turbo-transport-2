from dataclasses import dataclass

import requests

from search.data import DataProvider, RawNode, RawLine

# Functions annotated with this won't change their response much, if ever.
# We can cache these for the rest of the runtime of the program.
from functools import cache

# Functions annotated with this change their response fairly often.
from cachetools import cached, TTLCache


class DpmpDataProvider(DataProvider):
    api_key = ""

    def __init__(self, apikey: str):
        self.api_key = apikey

    def fetch(self, thing):
        return requests.request(
            "POST",
            f'https://online.dpmp.cz/api/{thing}',
            json=('{"key":"' + self.api_key + '"}')
        ).json()

    @cache
    def get_stations(self):
        json_stations = self.fetch("stations")
        processed_stations = []

        for station in json_stations:
            number = station['number']
            name = station['name']
            lat = station['gps_latitude']
            lon = station['gps_longitude']
            platforms = station['platforms']
            meta = {
                'platforms': [
                    DpmpPlatform(
                        p['gps_latitude'],
                        p['gps_longitude'],
                        p['number']
                    )
                    for p in platforms
                ]
            }

            processed_stations.append(RawNode(number, name, lat, lon))

        return processed_stations

    @cache
    def get_lines(self):
        return self.fetch("lines")

    @cached(cache=TTLCache(maxsize=64, ttl=30))
    def get_all_vehicle_state(self):
        return self.fetch("buses")

    @cached(cache=TTLCache(maxsize=64, ttl=30))
    def get_line_connections(self, line):
        return self.fetch(f"currentConnections?line={line}")

    @cached(cache=TTLCache(maxsize=64, ttl=30))
    def get_station_connections(self, station):
        return self.fetch(f"stationConnections?station={station}")

    @cached(cache=TTLCache(maxsize=64, ttl=30))
    def get_connection(self, line, vehicle):
        return self.fetch(f"busConnectionDetail?line={line}&number={vehicle}")
