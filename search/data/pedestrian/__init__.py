import requests
import osmnx as ox

from search.data import AbstractDataProvider, TransportMethod

from functools import cache


class PedestrianDataProvider(AbstractDataProvider):
    north = 0
    south = 0
    west = 0
    east = 0
    custom_filter = ""

    def __init__(self, north, south, west, east, custom_filter):
        self.custom_filter = custom_filter
        self.north = north
        self.south = south
        self.west = west
        self.east = east

    # Get nodes
    @cache
    def get_graph(self, provider_name):
        # Todo custom edges and nodes, to conform with Node and Edge classes

        G = ox.graph_from_bbox(
            bbox=(self.north, self.south, self.east, self.west),
            network_type='walk',
            simplify=True,
            truncate_by_edge=False,
            custom_filter=self.custom_filter
        )
        return G

    # These don't even make sense here...
    def get_all_vehicle_state(self): return []
    def get_line_connections(self, line): return []
    def get_station_connections(self, station): return []
    def get_connection(self, line, vehicle): return []
