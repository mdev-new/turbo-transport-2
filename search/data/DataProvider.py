from abc import ABC, abstractmethod


# Based on the DPMP API.

class DataProvider(ABC):
    @abstractmethod
    def get_stations(self):
        pass

    @abstractmethod
    def get_lines(self):
        pass

    @abstractmethod
    def get_all_vehicle_state(self):
        pass

    @abstractmethod
    def get_line_connections(self, line):
        pass

    @abstractmethod
    def get_station_connections(self, station):
        pass

    @abstractmethod
    def get_connection(self, line, vehicle):
        pass
