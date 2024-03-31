import requests
import osmnx as ox

from .. import AbstractDataProvider, TransportMethod

from functools import cache

# Todo gas prices, map
# Todo road state (take into account any accidents etc)

class CarDataProvider(AbstractDataProvider):
    north = 0
    south = 0
    west = 0
    east = 0

    def __init__(self, north, south, west, east, custom_filter):
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
            network_type='drive_service',
            simplify=True,
            truncate_by_edge=False
        )
        return G

    # These don't even make sense here...
    def get_all_vehicle_state(self): return []
    def get_connection(self, line, vehicle): return []
