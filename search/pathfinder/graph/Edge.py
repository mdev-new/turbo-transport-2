from search.misc.utils import overlapping_pairs, haversine


class Edge:
    length = 0.0
    transport_method = "foot"
    transport_network = "dpmp"
    public_line = -1

    def __init__(self, transport_method, transport_network, public_line=-1, path=None):
        self.length = 0.0
        self.public_line = public_line
        self.transport_method = transport_method
        if path is not None:
            for a, b in overlapping_pairs(path):
                self.length += haversine(a, b)

