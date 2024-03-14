from search.pathfinder.graph import AdjacentList
from search.pathfinder.graph import StationLookup
from search.pathfinder.graph import Node, Edge
from search.misc.utils import overlapping_pairs
import pickle
from pathlib import Path

type NodeCompatible = int | str | Node | GraphEntry
type NodeId = int | str


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


class Graph:
    adjList = None
    station_lookup = None

    def __init__(self, data_providers):
        self.station_lookup = StationLookup()
        self.adjList = AdjacentList()

        # TODO: Graph connectivity - a foot route will connect to
        # bus stops for example

        for p_name, provider in data_providers.items():
            stations = provider.get_stations()
            lines = provider.get_lines()

            for station in stations:
                # Todo handle id duplicates across providers
                number = station.identifier
                self.station_lookup[number] = Node(number, station.lat, station.lon, station.name)

            for line in lines:
                for prev, cur in overlapping_pairs(line.stops):
                    if all(x in self.station_lookup for x in [prev.identifier, cur.identifier]):
                        new_edge = Edge('public', p_name, line.number)
                        prev_node = self.station_lookup[prev.identifier]
                        cur_node = self.station_lookup[cur.identifier]
                        self.setBoth(prev_node, cur_node, new_edge)

    def makeNode(self, node: Node | NodeId):
        if node not in self.adjList:
            self.adjList[node] = []

    def setOne(self, n1: Node | NodeId, n2: Node | NodeId, edge: Edge):
        self.makeNode(n1)
        self.adjList[n1].append(GraphEntry(n2, edge))

    def setBoth(self, n1: Node | NodeId, n2: Node | NodeId, edge: Edge):
        self.setOne(n1, n2, edge)
        self.setOne(n2, n1, edge)

    # Return node's links regardless of the node being a number or a Node obj
    def getLinks(self, node: Node | NodeId):
        return self.adjList[node]

    def getNode(self, node: Node):
        if isinstance(node, Node | NodeId):
            return self.station_lookup[node]
        elif isinstance(node, GraphEntry):
            return self.station_lookup[node.node]

    # Return timetable, starting in `node`, for all lines
    def get_timetable_from_node(self, node: Node):
        pass

#    def get_timetable_for_line(self, line: int):
#        return self.timetables[line]

    def print(self):
        for node, values in self.adjList.items():
            print(
                f'{self.station_lookup[node].name} -> {[(self.station_lookup[entry.node].name, entry.edge) for entry in values]}'
            )

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    # Todo maybe write to database
    @staticmethod
    def new(filename, *args, **kwargs):
        if Path(filename).is_file():
            with open(filename, 'rb') as f:
                return pickle.load(f)
        else:
            g = Graph(*args, **kwargs)
            g.save(filename)
            return g
