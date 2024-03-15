from django.shortcuts import render

from search.pathfinder.graph.Graph import Graph
from search.pathfinder.PathFinder import PathFinder
# from search.misc.utils import overlapping_pairs

from search.data import DpmpDataProvider, OnFootDataProvider
from search.data import CDDataProvider
from search.data import KhkDataProvider

from search.misc import constants

data_providers = {
    'dpmp': DpmpDataProvider("3e86570d-56a1-4ec1-8012-c1a9f98d18cc"),
    #    'cd': CDDataProvider(),
    #    'khk': KhkDataProvider(),
    #    'foot': OnFootDataProvider(constants.OVERPASS_REQUEST)
}

graph = Graph(data_providers)
#graph.print()
pathfinder = PathFinder(graph, data_providers)


# Graph.new('hello.dat', data_providers)


def index(req):
    return render(req, 'search.html')


def search(req):
    data_source = req.POST if req.method == "POST" else req.GET

    source = data_source.get('from')
    dest = data_source.get('to')
    walk_speed = float(data_source.get('walk_speed'))
    urgency = int(data_source.get('urge'))

    if data_source.get('request_source') == 'link_history':
        search_idx = data_source.get('search_idx')  # todo pull from db and all that

    # bus_snapshot = get_dpmp("buses")
    path = list(pathfinder.search(source, dest, walk_speed, urgency))
    # print(path)

    _context = {
        'results': path[1:],
        'query': f'z:{source} kam:{dest} rychlost_chuze:{walk_speed} nutnost:{urgency}'
    }

    return render(req, '_results.html', _context)


def get_stations(req):
    global graph
    return render(
        req,
        '_stations.html',
        {
            'stations': [station.name for s_id, station in graph.station_lookup.items()]
        }
    )
