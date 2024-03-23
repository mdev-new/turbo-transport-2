from dataclasses import dataclass

import requests

from search.data import AbstractDataProvider, RawLine, RawRouteStop

# Functions annotated with this won't change their response much, if ever.
# We can cache these for the rest of the runtime of the program.
from functools import cache

# Functions annotated with this change their response fairly often.
from cachetools import cached, TTLCache

from search.data.Node import Node


class DpmpDataProvider(AbstractDataProvider):
    api_key = ""

    def __init__(self, apikey: str):
        self.api_key = apikey

    def is_on_foot(self):
        return False

    def fetch(self, thing):
        return requests.request(
            "POST",
            f'https://online.dpmp.cz/api/{thing}',
            json=('{"key":"' + self.api_key + '"}')
        ).json()

    @cache
    def get_nodes(self):
        stations_object = self.fetch("stations")

        return [
            Node(
                station['gps_latitude'],
                station['gps_longitude'],
                station['name'],
                station['number']
            ) for station in stations_object
        ]

    # TO FUCKING DO
    @cache
    def get_lines(self):
        fetched_lines = self.fetch("lines")
        processed_lines = []
        for line in fetched_lines:
            processed_stops = []
            for s in line['stops']:
                processed_stops.append(RawRouteStop(s['number'], s['name'], s['codes']))

            processed_lines.append(RawLine(line['number'], processed_stops))

        return processed_lines

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
