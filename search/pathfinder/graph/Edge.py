from search.misc.utils import overlapping_pairs, haversine


class Edge:
    length = 0.0
    transport_method = "foot"
    public_line = -1

    def __init__(self, transport_method, public_line=-1, path=None):
        self.length = 0.0
        self.public_line = public_line
        if path is not None:
            for a, b in overlapping_pairs(path):
                self.length += haversine(a, b)
