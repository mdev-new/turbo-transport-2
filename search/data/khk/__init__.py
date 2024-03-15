from search.data import AbstractDataProvider


# Kralovehradecky kraj most likely doesn't provide public data about
# buses on-the-go.
# So, everything will have to be pulled out from the timetable.

class KhkDataProvider(AbstractDataProvider):

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
