from django.shortcuts import render

from .Graph import Graph
from .PathFinder import PathFinder
from .utils import get_dpmp, overlapping_pairs

# from . import constants
# from .utils import get_overpass
# map = get_overpass(constants.OVERPASS_REQUEST)

# Todo
# - Timetables
# - Search
# - On foot
# - Link buses
# - Trains
# - Maps - navigation
# - Personalization - saving last searches
# - Search in the future?

# Far todo
# - saving the graph to disk
# - Kralovehradecky kraj (datakhk.cz)

# Frontend
# - A map

stations = get_dpmp("stations").json()
lines = get_dpmp("lines").json()
graph = Graph(lines, stations, {})
pathfinder = PathFinder(graph)


def index(req):
    return render(req, 'search.html')


def search(req):

    data_source = req.POST if req.method == "POST" else req.GET

    source = data_source.get('from')
    dest = data_source.get('to')
    walk_speed = int(data_source.get('walk_speed')) * 2.5
    urgency = int(data_source.get('urge'))

    bus_snapshot = None  # get_dpmp("buses")
    path = list(pathfinder.search(source, dest, bus_snapshot, walk_speed, urgency))

    _context = {
        'results': path[1:],
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
