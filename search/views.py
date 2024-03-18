from django.shortcuts import render

from search.data import DpmpDataProvider, OnFootDataProvider
from search.data import CDDataProvider
from search.data import KhkDataProvider

from search.data import Edge

from search.misc import constants
from search.misc.utils import overlapping_pairs

import matplotlib.pyplot as plt

import networkx as nx

data_providers = {
    'dpmp': DpmpDataProvider("3e86570d-56a1-4ec1-8012-c1a9f98d18cc"),
    #    'cd': CDDataProvider(),
    #    'khk': KhkDataProvider(),
    #    'foot': OnFootDataProvider(constants.OVERPASS_REQUEST)
}

G = nx.Graph()

for p_name, p in data_providers.items():
    nodes = p.get_nodes()
    G.add_nodes_from([(n.name, n.as_dict()) for n in nodes])

    for line in p.get_lines():
        for prev, cur in overlapping_pairs(line.stops):
            if all(x in nodes for x in [prev.name, cur.name]):
                new_edge = Edge(p_name, line.number)
                G.add_edge(prev.name, cur.name, **new_edge.as_dict())


def index(req):
    return render(req, 'search.html')


def search(req):
    data_source = req.POST if req.method == "POST" else req.GET

    source = data_source.get('from')
    target = data_source.get('to')
    walk_speed = float(data_source.get('walk_speed'))
    urgency = int(data_source.get('urge'))

    if data_source.get('request_source') == 'link_history':
        search_idx = data_source.get('search_idx')  # todo pull from db and all that

    def edge_weight(n1, n2, edge):
        # print(n1, n2, edge)
        return 1

    path = nx.shortest_path(G, source, target, weight=edge_weight)
    path_graph = nx.path_graph(path)
    newpath = [
        [ea, G.edges[ea[0], ea[1]]['line']]
        for ea in path_graph.edges()
    ]

    # print(path)

    _context = {
        'results': newpath,
        'query': f'z:{source} kam:{target} rychlost_chuze:{walk_speed} nutnost:{urgency}'
    }

    return render(req, '_results.html', _context)


def get_stations(req):
    return render(
        req,
        '_stations.html',
        {
            'stations': G.nodes()
        }
    )
