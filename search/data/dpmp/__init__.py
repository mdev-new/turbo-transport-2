from dataclasses import dataclass

import networkx as nx
import requests

from search.data import AbstractDataProvider, Node, Edge, TransportMethod

# Functions annotated with this won't change their response much, if ever.
# We can cache these for the rest of the runtime of the program.
from functools import cache

# Functions annotated with this change their response fairly often.
from cachetools import cached, TTLCache

from search.misc.utils import overlapping_pairs


class DpmpDataProvider(AbstractDataProvider):
    api_key = ""

    def __init__(self, apikey: str):
        self.api_key = apikey

    def fetch(self, thing):
        return requests.post(
            f'https://online.dpmp.cz/api/{thing}',
            json=('{"key":"' + self.api_key + '"}')
        ).json()

    # TODO TODO TODO
    @cache
    def get_graph(self, provider_name):

        G = nx.MultiDiGraph()

        nodes = [
            Node(s['gps_latitude'], s['gps_longitude'], s['name'], s['number'])
            for s in self.fetch('stations')
        ]

        G.add_nodes_from([(n.name, n.as_dict()) for n in nodes])

        #
        # lines = [
        #
        # ]
        #
        #
        # for line in lines:
        #     for prev, cur in overlapping_pairs(line.stops):
        #         if all(x in nodes for x in [prev.name, cur.name]):
        #             new_edge = Edge(
        #                 TransportMethod.CITY_TRANSPORT,
        #                 provider_name,
        #                 line.number
        #             )
        #             G.add_edge(prev.name, cur.name, **new_edge.as_dict())

        return G

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_all_vehicle_state(self):
        return self.fetch("buses")

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_line_connections(self, line):
        return self.fetch(f"currentConnections?line={line}")

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_station_connections(self, station):
        return self.fetch(f"stationConnections?station={station}")

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_connection(self, line, vehicle):
        return self.fetch(f"busConnectionDetail?line={line}&number={vehicle}")
