from search.utils import overlapping_pairs, haversine


class Edge:
    length = 0.0
    transport_method = "foot"
    public_line = -1

    def __init__(self, transport_method, public_line=-1, path=None):
        self.public_line = public_line
        self.transport_method = transport_method
        self.length = 0.0
        if path is not None:
            for a, b in overlapping_pairs(path):
                self.length += haversine(a, b)


class Node:
    number = 0
    lat = 0.0
    lon = 0.0
    name = ""
    platform_for = -1
    platform_number = -1

    def __init__(self, number: int, lat, lon, name, platform_for=-1, platform_number=-1):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.number = number
        self.platform_for = platform_for
        self.platform_number = platform_number

    def __eq__(self, other):

        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, int):
            return self.number == other
        else:
            return self.number == other.number

    def __hash__(self):
        return hash(self.number)


class GraphEntry:
    node = None
    edge = None

    def __init__(self, node, edge):
        self.node = node
        self.edge = edge

    def __eq__(self, other):
        if isinstance(other, GraphEntry):
            return self.node == other.node
        else:
            return self.node == other

    def __hash__(self):
        return hash((self.node, self.edge))
