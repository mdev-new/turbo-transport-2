from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from .Node import Node

# Based on the DPMP API.

@dataclass
class Position:
    lat: float
    lon: float


@dataclass
class RawRouteStop:
    identifier: int
    name: str
    codes: list[int]


@dataclass
class RawLine:
    number: int  # Bus line number
    stops: list[RawRouteStop]


@dataclass
class RawRoute:
    line: int
    route: list[Position]


# Vehicle state
@dataclass
class RawVehicleState:
    line: int
    lat: float
    lon: float
    destination_stop: int
    current_stop: int
    time_diff: int
    speed: float = 0.0


# Connection
@dataclass
class RawConnectionStop:
    number: int
    index: int
    lat: float
    lon: float
    distance: int
    arrival_time: int  # UNIX timestamp
    departure_time: int
    name: str = ""
    platform: int = 1


@dataclass
class RawConnection:
    line_number: int
    connection_number: int
    stops: list[RawConnectionStop]
    route_start_time: int
    route_end_time: int
    bus_info: RawVehicleState = None


class AbstractDataProvider(ABC):
    @abstractmethod
    def get_nodes(self) -> list[Node]: pass

    @abstractmethod
    def get_lines(self) -> list[RawLine]: pass

    @abstractmethod
    def get_line_connections(self, line) -> list[RawConnection]: pass

    @abstractmethod
    def get_station_connections(self, station): pass

    @abstractmethod
    def get_connection(self, line, vehicle): pass

    @abstractmethod
    def get_all_vehicle_state(self) -> list[RawVehicleState]: pass

    @abstractmethod
    def is_on_foot(self) -> bool: pass
