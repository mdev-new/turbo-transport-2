from abc import ABC, abstractmethod
from dataclasses import dataclass


# Based on the DPMP API.

@dataclass
class RawPlatform:
    number: int
    lat: float
    lon: float


@dataclass
class RawNode:
    identifier: int | str
    name: str
    lat: float
    lon: float
    platforms: list[RawPlatform]
    meta: dict  # Implementation custom metadata


@dataclass
class RawLine:
    stops = []
    number = 0


# TODO
@dataclass
class RawVehicleState:
    lat: float
    lon: float
    line: int
    speed: float = 0.0


@dataclass
class RawStop(RawNode):
    index: int
    distance: int
    arrivalTime: int  # UNIX timestamp
    departureTime: int
    platform: int = 1


@dataclass
class RawConnectionDetail:
    stops: list[RawStop]


@dataclass
class RawConnection:
    connections: list[RawConnectionDetail]
    vehicle_status: RawVehicleState


class DataProvider(ABC):
    @abstractmethod
    def get_stations(self) -> list[RawNode]:
        pass

    @abstractmethod
    def get_lines(self) -> list[RawLine]:
        pass

    @abstractmethod
    def get_line_connections(self, line) -> list[RawConnection]:
        pass

    @abstractmethod
    def get_station_connections(self, station):
        pass

    @abstractmethod
    def get_connection(self, line, vehicle):
        pass

    @abstractmethod
    def get_all_vehicle_state(self) -> list[RawVehicleState]:
        pass
