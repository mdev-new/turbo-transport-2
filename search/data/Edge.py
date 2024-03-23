from search.misc.utils import overlapping_pairs, haversine


class Edge:
    transport: str
    public_line: int = None
    length: float = None

    def __init__(self, transport_method, public_line=None, path=None):
        self.transport = transport_method
        self.public_line = public_line
        if path is not None:
            self.length = 0.0
            for a, b in overlapping_pairs(path):
                self.length += haversine(a, b)

    def as_dict(self):
        return {
            'transport': self.transport,
            'line': self.public_line,
            'length': self.length
        }
