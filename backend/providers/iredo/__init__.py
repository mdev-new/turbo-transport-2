from dataclasses import dataclass
from os import walk

import requests
import networkx as nx

import xml.etree.ElementTree as ElemTree

from .. import AbstractDataProvider, Node

from zipfile import ZipFile

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

        # Load the NeTEx
        for timetable_zip in ['DrahyMestske', 'GVD2024', 'VerejnaLinkovaDoprava']:
            with ZipFile(f'data/NeTEx_{timetable_zip}.zip') as zf:
                for file in zf.namelist():
                    with zf.open(file) as f:
                        roots.append(ElemTree.parse(f).getroot())

        for root in roots:
            pass

        return G

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_all_vehicle_state(self):
        return self.fetch("service/position")

    @cached(cache=TTLCache(maxsize=64, ttl=45))
    def get_connection(self, line, vehicle):
        return self.fetch(f"servicedetail?id={vehicle}")
