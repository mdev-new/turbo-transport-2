from django.shortcuts import render

from search.pathfinder.graph.Graph import Graph
from search.pathfinder.PathFinder import PathFinder
# from search.misc.utils import overlapping_pairs

from search.data import DpmpDataProvider
from search.data import CDDataProvider
from search.data import KhkDataProvider

data_providers = {
    'dpmp': DpmpDataProvider("3e86570d-56a1-4ec1-8012-c1a9f98d18cc"),
    'cd': CDDataProvider(),
    'khk': KhkDataProvider()
}

graph = Graph(data_providers)
pathfinder = PathFinder(graph)


def index(req):
    return render(req, 'search.html')


def _dedupe(data):
    return data
    # is_not_none = lambda x: x is not None
    # no_duplicates = lambda last, cur: last if ((last.edge.transport_method == 'public' and cur.edge.transport_method == 'public' and last.edge.public_line != cur.edge.public_line) or cur.edge.transport_method != last.edge.transport_method) else None
    #
    # return list(filter(is_not_none, map(no_duplicates, overlapping_pairs(data))))


def search(req):
    data_source = req.POST if req.method == "POST" else req.GET

    if data_source.get('request_source') == 'link_history':
        search_idx = data_source.get('search_idx')  # todo pull from db and all that
    else:
        source = data_source.get('from')
        dest = data_source.get('to')
        walk_speed = float(data_source.get('walk_speed'))
        urgency = int(data_source.get('urge'))

    # bus_snapshot = get_dpmp("buses")
    path = list(pathfinder.search(source, dest, walk_speed, urgency))

    _context = {
        'results': _dedupe(path[1:]),
        'query': f'z:{source} kam:{dest} rychlost_chuze:{walk_speed} nutnost:{urgency}'
    }

    return render(req, '_results.html', _context)


def get_stations(req):
    global stations
    return render(
        req,
        '_stations.html',
        {
            'stations': [station['name'] for station in stations]
        }
    )
