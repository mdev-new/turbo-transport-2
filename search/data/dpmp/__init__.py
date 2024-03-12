import requests

from search.data.DataProvider import DataProvider

from functools import cache


class DpmpDataProvider(DataProvider):
    api_key = ""

    def __init__(self, apikey):
        self.api_key = apikey

    @cache  # Todo: limit this cache to smth like two minutes of lifetime
    def _fetch(self, thing):
        return requests.request(
            "POST",
            f'https://online.dpmp.cz/api/{thing}',
            json=('{"key":"' + self.api_key + '"}')
        ).json()

    def get_stations(self):
        return self._fetch("stations")

    def get_lines(self):
        return self._fetch("lines")

    def get_all_vehicle_state(self):
        return self._fetch("buses")

    def get_line_connections(self, line):
        return self._fetch(f"currentConnections?line={line}")

    def get_station_connections(self, station):
        pass

    def get_connection(self, line, vehicle):
        pass
