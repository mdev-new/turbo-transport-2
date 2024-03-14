from search.pathfinder.graph import GraphEntry, Node


class AdjacentList(dict):
    def get_index(self, k):
        if isinstance(k, int):
            return k  # we already have the index

        elif isinstance(k, str):
            for key, value in self.stations.items():
                if value.name == k:
                    return key

        elif isinstance(k, Node):
            for key, val in self.stations.items():
                if val == k:
                    return key

        elif isinstance(k, GraphEntry):
            for station_number, station in self.stations.items():
                if station.identifier == k.node:
                    return station_number

        print(f"Didn't find a key: {k.identifier}")

    def __getitem__(self, k: int | str | Node | GraphEntry):
        return super().__getitem__(self.get_index(k))

    def __setitem__(self, k: int, v):
        return super().__setitem__(k, v)
