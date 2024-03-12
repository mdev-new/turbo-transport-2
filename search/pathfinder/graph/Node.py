
class Node:
    identifier = ""  # An unique identifier - something like DPMP-021
    lat = 0.0
    lon = 0.0
    name = ""
    available_transport_methods = []
    platform_for = -1
    platform_number = -1

    def __init__(self, identifier: int, lat: float, lon: float, name: str, platform_for=-1, platform_number=-1):
        self.identifier = identifier
        self.lat = lat
        self.lon = lon
        self.name = name
        self.platform_for = platform_for
        self.platform_number = platform_number

    def __eq__(self, other):

        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, int):
            return self.identifier == other
        else:
            return self.identifier == other.identifier

    def __hash__(self):
        return self.identifier

