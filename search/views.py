from astar import AStar
from django.shortcuts import render

from .utils import get_dpmp, get_overpass, haversine, overlapping_pairs


# from .constants import OVERPASS_REQUEST
# map = get_overpass(OVERPASS_REQUEST)

# Todo
# - Timetables
# - Search
# - Maps

# Frontend
# - A map

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
    platformFor = -1
    platform_number = -1

    def __init__(self, number: int, lat, lon, name, platform_for=-1, platform_number=-1):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.number = number
        self.platformFor = platform_for
        self.platform_number = platform_number

    def __int__(self):
        return self.number


class GraphEntry:
    node = None
    edge = None

    def __init__(self, node, edge):
        self.node = node
        self.edge = edge

    def __int__(self):
        return self.node.number


# Todo make sense of the edges in this graph
# I think the edge is always in n1.edge
# or more like n2.edge <- THIS
# TODO TODO make sense of passing the actual nodes around
# Maybe pass around only ints?
class Graph:
    adjList = {}
    station_lookup = {}
    timetables = {}

    def __init__(self, _lines, _stations, _timetables):
        self.station_lookup = {}
        self.timetables = _timetables

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

        for line in _lines:
            stops = line['stops']
            for prev, cur in overlapping_pairs(stops):
                self.setBoth(prev['number'], cur['number'], Edge('public', line['number']))

    def makeNode(self, node):
        if node not in self.adjList:
            self.adjList[node] = []

    # So.... n1 is always an integer but n2 is an graph entry?
    def setOne(self, n1, n2, edge):
        self.makeNode(n1)
        self.adjList[n1].append(GraphEntry(n2, edge))

    def setBoth(self, n1, n2, edge):
        self.setOne(n1, n2, edge)
        self.setOne(n2, n1, edge)

    # Return node's links regardless of the node being a number or a Node obj
    def getLinks(self, node):
        return self.adjList[int(node)]

    def getNode(self, node):
        return self.station_lookup[int(node)]

    # Return timetable, starting in `node`, for all lines
    def get_timetable_from_node(self, node):
        pass

    def get_timetable_for_line(self, line):
        return self.timetables[line]

    def print(self):
        for node, values in self.adjList.items():
            print(
                f'{self.station_lookup[node].name} -> {[(self.station_lookup[entry.node].name, entry.edge) for entry in values]}'
            )


class PathFinder(AStar):
    bus_snapshot = None

    def __init__(self, graph):
        self.bus_snapshot = None
        self.graph = graph
        # self.graph.print()

    def neighbors(self, node):
        return self.graph.getLinks(node)

    # The distance (weight) between two nodes
    def distance_between(self, n1, n2):
        # Todo get the time to get from n1 to n2
        # todo for buses, pull this from the time table
        # for distance on foot, look at the length of the edge
        pass

    # An estimate of the distance/cost between current node and the end
    def heuristic_cost_estimate(self, current, goal):
        current_node: Node = self.graph.getNode(current)
        goal_node: Node = self.graph.getNode(goal)
        distance_between = haversine([current_node.lat, current_node.lon], [goal_node.lat, goal_node.lon])
        return distance_between / 20  # let's assume 20 km/h to be the avg speed

    def is_goal_reached(self, current: GraphEntry | str, goal: GraphEntry | str):
        return int(current) == int(goal)

    def search(self, start, goal, bus_snapshot, reverse_path=False):
        self.bus_snapshot = bus_snapshot
        return self.astar(start, goal, reverse_path)


stations = get_dpmp("stations").json()
lines = get_dpmp("lines").json()
pathfinder = PathFinder(Graph(lines, stations, {}))


def index(req):
    return render(req, 'index.html')


def search(req):
    source = req.POST.get('from')
    dest = req.POST.get('to')
    walk_speed = req.POST.get('walk_speed')
    urgency = req.POST.get('urge')

    # path = pathfinder.search(source, dest, get_dpmp("buses"))

    _context = {
        'results': [
            # path
        ],
        'text': f'z:{source} kam:{dest} rychlost_chuze:{walk_speed} nutnost:{urgency}'
    }
    return render(req, '_results.html', _context)
