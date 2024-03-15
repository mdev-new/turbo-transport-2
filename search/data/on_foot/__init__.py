import requests

from search.data import AbstractDataProvider, RawStop, RawLine

from functools import cache


class OnFootDataProvider(AbstractDataProvider):
    request_addr = ""
    data = {}

    def __init__(self, request_addr):
        self.request_addr = request_addr
        self.data = self.fetch(self.request_addr)

    def fetch(self, addr):
        return requests.request("GET", addr).json()

    # Get nodes
    @cache
    def get_stations(self):
        return []

    # Get edges/paths between nodes
    @cache
    def get_lines(self):
        return []

    # Doesn't make sense here...
    def get_all_vehicle_state(self):
        return []

    # Basically return the neighbours?
    def get_line_connections(self, line):
        return []

    # Return neighboring edges?
    def get_station_connections(self, station):
        return []

    # Doesn't make sense here...
    def get_connection(self, line, vehicle):
        return []
