from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TypedDict
from search.misc.utils import overlapping_pairs, haversine
import networkx as nx

from enum import Enum


class TransportMethod(Enum):
    FOOT = 0
    BIKE = 1
    CITY_TRANSPORT = 2
    LINK_BUS = 3
    TRAIN = 4
    CAR = 5

class NodeData(TypedDict):
    lat: float
    lon: float
    name: str
    ident: None | object


class Node:
    lat = 0.0
    lon = 0.0
    ident = None  # Identifier that's specific to every transport company
    name = ""

    def __init__(self, lat: float, lon: float, name: str, ident=None):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.ident = ident

    # For serializing to graph node properties
    def as_dict(self) -> NodeData:
        return {
            'lat': self.lat,
            'lon': self.lon,
            'name': self.name,
            'ident': self.ident
        }


class Edge:
    transport_method: TransportMethod = None
    transport_carrier: str = None
    public_line: int = None
    public_number: int = None
    length: float = None
    start_offset: int = 0  # After how many seconds after 00:00 does the thing depart

    def __init__(self, transport_method=TransportMethod.FOOT, carrier='pedestrian', public_line=None, path=None):
        self.transport_method = transport_method
        self.transport_carrier = carrier
        self.public_line = public_line
        if path is not None:
            self.length = 0.0
            for a, b in overlapping_pairs(path):
                self.length += haversine(*a, *b)

    # For serializing to graph edge properties
    def as_dict(self):
        return {
            'method': self.transport_method,
            'carrier': self.transport_carrier,
            'line': self.public_line,
            'length': self.length,
            'start_time': self.start_offset
        }


class Connection:
    pass


class VehicleState:
    pass


class Line:
    pass


class AbstractDataProvider(ABC):
    @abstractmethod
    def get_graph(self, provider_name: str) -> nx.MultiDiGraph: pass

    @abstractmethod
    def get_connection(self, line, vehicle) -> Connection: pass

    @abstractmethod
    def get_all_vehicle_state(self) -> list[VehicleState]: pass
