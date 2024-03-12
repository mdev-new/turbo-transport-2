from search.data import DataProvider

# Kralovehradecky kraj most likely doesn't provide public data about
# buses on-the-go.
# So, everything will have to be pulled out from the timetable.

class KhkDataProvider(DataProvider):

    def get_stations(self):
        pass

    def get_lines(self):
        pass

    def get_all_vehicle_state(self):
        pass

    def get_line_connections(self, line):
        pass

    def get_station_connections(self, station):
        pass

    def get_connection(self, line, vehicle):
        pass
