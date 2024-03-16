type NodeId = int


class Node:
    identifier: NodeId  # An unique identifier - something like DPMP-021
    lat = 0.0
    lon = 0.0
    name = ""

    def __init__(self, identifier: NodeId, lat: float, lon: float, name: str, platform_for=-1, platform_number=-1):
        self.identifier = identifier
        self.lat = lat
        self.lon = lon
        self.name = name
        self.platform_for = platform_for
        self.platform_number = platform_number

    def __hash__(self) -> NodeId:
        return self.identifier
