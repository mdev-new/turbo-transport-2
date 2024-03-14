from astar import AStar

from search.pathfinder.graph import Node, GraphEntry
from search.misc.utils import haversine
from .graph.Graph import NodeId

# Todo: Distance/weight between

class PathFinder(AStar):
    graph = None
    data_providers = None
    walk_speed = 5
    urge = 0

    def __init__(self, graph, data_providers):
        self.graph = graph
        self.data_providers = data_providers

    def neighbors(self, node: Node | GraphEntry):
        return self.graph.getLinks(self.graph.getNode(node))

    # The distance (weight) between two nodes
    def distance_between(self, n1: GraphEntry, n2: GraphEntry):
        # for distance on foot, look at the length of the edge
        edge = n2.edge
        if edge.length is not None and edge.transport_method == 'foot':
            return n2.edge.length / self.walk_speed
        else:

            line_connections = self.data_providers[edge.transport_network].get_line_connections(edge.public_line)

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

    def is_goal_reached(self, current: GraphEntry, goal: GraphEntry):
        node_a = self.graph.getNode(current)
        node_b = self.graph.getNode(goal)
        return node_a.identifier == node_b.identifier

    def search(self, start: str, goal: str, walk_speed, urge):
        self.walk_speed = walk_speed
        self.urge = urge
        return self.astar(self.graph.getNode(start), self.graph.getNode(goal))
