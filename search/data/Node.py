
class Node:
    lat = 0.0
    lon = 0.0
    name = ""
    ident = None

    def __init__(self, lat: float, lon: float, name: str, ident=None):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.ident = ident

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        else:
            return self.name == other.name

    def as_dict(self):
        return {
            'lat': self.lat,
            'lon': self.lon,
            'name': self.name,
            'ident': self.ident
        }
