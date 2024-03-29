from django.shortcuts import render

import networkx as nx

from . import graph
from .misc.constants import KMH_TO_MS

from functools import partial

G = graph.get_graph("graph.graphml")


def index(req):
    return render(req, 'search.html')


def search(req):
    request_data = req.POST if req.method == "POST" else req.GET

    source = request_data.get('from')
    target = request_data.get('to')
    walk_speed = float(request_data.get('walk_speed'))
    urgency = int(request_data.get('urge'))

    if request_data.get('request_source') == 'link_history':
        search_idx = request_data.get('search_idx')  # todo pull from db and all that

    wt_func = partial(graph.edge_weight, {
        'walk_speed': walk_speed,
        'cycle_speed': 18 * KMH_TO_MS
    })

    path = nx.shortest_path(G, source, target, weight=wt_func)
    path_graph = nx.path_graph(path)
    newpath = [
        [ea, G.edges[ea[0], ea[1]]['line']]
        for ea in path_graph.edges()
    ]

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
