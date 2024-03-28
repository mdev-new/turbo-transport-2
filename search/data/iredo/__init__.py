from dataclasses import dataclass
from os import walk

import requests
import networkx as nx

import xml.etree.ElementTree as ET

from search.data import AbstractDataProvider, Node

# Functions annotated with this won't change their response much, if ever.
# We can cache these for the rest of the runtime of the program.
from functools import cache

# Functions annotated with this change their response fairly often.
from cachetools import cached, TTLCache


class IredoDataProvider(AbstractDataProvider):
    def __init__(self):
        pass

    def fetch(self, thing):
        return requests.get(
            f'https://tabule.oredo.cz/idspublicservices/api/{thing}'
        ).json()

    @cache
    def get_graph(self, provider_name):

        G = nx.MultiDiGraph()

        stations = self.fetch('station')

        roots = []

        for datadir in ['NeTEx_DrahyMestske', 'NeTEx_GVD2024']:
            for (dirpath, dirnames, filenames) in walk(f'data/{datadir}'):
                for filename in filenames:
                    roots.append(ET.parse(filename).getroot())

        return G

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_all_vehicle_state(self):
        return self.fetch("service/position")

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_line_connections(self, line):
        raise NotImplementedError
        # return self.fetch(f"")

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_station_connections(self, station):
        return self.fetch(f"station/{station}/nextservices")

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_connection(self, line, vehicle):
        return self.fetch(f"servicedetail?id={vehicle}")
