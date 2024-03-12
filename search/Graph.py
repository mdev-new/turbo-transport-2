from search.NodeLookup import NodeLookup
from search.Node_Edge import GraphEntry, Node, Edge
from search.utils import overlapping_pairs
import pickle
from pathlib import Path


# fixme refactor
def get_station_index(self, k):
    if isinstance(k, int):
        return k  # we already have the index

    elif isinstance(k, str):
        for key, value in self.items():
            if value.name == k:
                return key

    elif isinstance(k, Node):
        for key, val in self.items():
            if val == k: return key

    elif isinstance(k, GraphEntry):
        for key, value in self.items():
            if value.number == k.node:
                return key

    print(f"Didn't find a key: {k.number}")


# fixme refactor
def get_adjlist_index(self, k):
    if isinstance(k, int):
        return k  # we already have the index

    elif isinstance(k, str):
        for key, value in self.stations.items():
            if value.name == k:
                return key

    elif isinstance(k, Node):
        for key, val in self.stations.items():
            if val == k: return key

    elif isinstance(k, GraphEntry):
        for station_number, station in self.stations.items():
            if station.number == k.node:
                return station_number

    print(f"Didn't find a key: {k.number}")


class Graph:
    adjList = None
    station_lookup = None
    timetables = {}
    savefile = ""

    def __init__(self, _lines, _stations, _timetables, savefile="save.pickle"):
        self.station_lookup = NodeLookup(get_station_index)
        self.timetables = _timetables
        self.savefile = savefile

        for station in _stations:
            name = station['name']
            # Todo add this to the list of nodes
            # when dealing with pedestrian travel
            # platforms = [
            #     Node(
            #         platform['gps_latitude'],
            #         platform['gps_longitude'],
            #         f'{name} - Platform {platform["number"]}',
            #         station['number'],
            #         platform["number"]
            #     )
            #     for platform in station['platforms']
            # ]

            number = station['number']
            lat = station['gps_latitude']
            lon = station['gps_longitude']

            self.station_lookup[number] = Node(number, lat, lon, name)

        self.adjList = NodeLookup(get_adjlist_index, stations=self.station_lookup)

        for line in _lines:
            stops = line['stops']
            for prev, cur in overlapping_pairs(stops):
                if (cur['number'] in self.station_lookup) and (prev['number'] in self.station_lookup):
                    self.setBoth(self.station_lookup[prev['number']], self.station_lookup[cur['number']], Edge('public', line['number']))

    # TODO
    # def __new__(cls, *args, **kwargs):
    #     if Path(savefile).is_file():
    #         with open(savefile, 'rb') as f:
    #             return pickle.load(f)
    #     else:
    #         return super().__new__(cls, args, kwargs)

    def makeNode(self, node: int):
        if node not in self.adjList:
            self.adjList[node] = []

    def setOne(self, n1: int, n2: int, edge: Edge):
        self.makeNode(n1)
        self.adjList[n1].append(GraphEntry(n2, edge))

    def setBoth(self, n1: int, n2: int, edge: Edge):
        self.setOne(n1, n2, edge)
        self.setOne(n2, n1, edge)

    # Return node's links regardless of the node being a number or a Node obj
    def getLinks(self, node: Node | GraphEntry | int):
        return self.adjList[node]

    def getNode(self, node: Node | GraphEntry | int):
        return self.station_lookup[node]

    # Return timetable, starting in `node`, for all lines
    def get_timetable_from_node(self, node: Node | GraphEntry):
        pass

    def get_timetable_for_line(self, line: int):
        return self.timetables[line]

    def print(self):
        for node, values in self.adjList.items():
            print(
                f'{self.station_lookup[node].name} -> {[(self.station_lookup[entry.node].name, entry.edge) for entry in values]}'
            )

    def save(self):
        with open(self.savefile, 'wb') as f:
            pickle.dump(self, f)
