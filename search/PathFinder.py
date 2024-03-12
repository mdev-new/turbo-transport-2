from astar import AStar

from search.Node_Edge import Node, GraphEntry
from search.utils import haversine, get_line_connections


# Todo: Distance/weight between

class PathFinder(AStar):
    bus_snapshot = None
    graph = None
    walk_speed = 5
    urge = 0

    def __init__(self, graph):
        self.bus_snapshot = None
        self.graph = graph

    def neighbors(self, node: GraphEntry | int | str):
        # print(f'got neighbours: {self.graph.getNode(node).name}')
        return self.graph.getLinks(node)

    # The distance (weight) between two nodes
    def distance_between(self, n1: GraphEntry, n2: GraphEntry):
        # for distance on foot, look at the length of the edge
        edge = n2.edge
        if edge.length is not None and edge.transport_method == 'foot':
            return n2.edge.length / self.walk_speed
        else:

            line_connections = get_line_connections(edge.public_line)

            # Todo select the right direction
            # Todo get departureTime for the next stop
            # and return current time - departure time

            return 5

    # An estimate of the distance/cost between current node and the end
    def heuristic_cost_estimate(self, current: GraphEntry, goal: GraphEntry):
        current_node: Node = self.graph.getNode(current)
        goal_node: Node = self.graph.getNode(goal)
        current_pos = [current_node.lat, current_node.lon]
        goal_pos = [goal_node.lat, goal_node.lon]

        # fixme this needs real data about avg speed, probably measures or live data
        return haversine(current_pos, goal_pos) / 18  # let's assume 18 km/h to be the avg speed

    def is_goal_reached(self, current, goal):
        node_a = self.graph.getNode(current)
        node_b = self.graph.getNode(goal)
        return node_a.number == node_b.number

    def search(self, start, goal, bus_snapshot, walk_speed, urge, reverse_path=False):
        self.bus_snapshot = bus_snapshot
        self.walk_speed = walk_speed
        self.urge = urge
        return self.astar(start, goal, reverse_path)
