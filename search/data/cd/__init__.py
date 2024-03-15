from search.data import AbstractDataProvider


class CDDataProvider(AbstractDataProvider):

    def get_stations(self):
        return []

    def get_lines(self):
        return []

    def get_all_vehicle_state(self):
        return []

    def get_line_connections(self, line):
        return []

    def get_station_connections(self, station):
        return []

    def get_connection(self, line, vehicle):
        return []
