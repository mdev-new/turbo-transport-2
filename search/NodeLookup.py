from search.Node_Edge import GraphEntry


class NodeLookup(dict):  # dicts take a mapping or iterable as their optional first argument
    index_fn = None

    def __init__(self, index_fn, **kwargs):
        self.index_fn = index_fn

        for k, v in kwargs.items():
            setattr(self, k, v)

        super().__init__()

    def __getitem__(self, k: int | str | GraphEntry):
        return super(NodeLookup, self).__getitem__(self.index_fn(self, k))

    def __setitem__(self, k: int, v):
        return super(NodeLookup, self).__setitem__(k, v)
