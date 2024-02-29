from django.shortcuts import render
from .work import get_buses, aStar

import pyrosm

osm = pyrosm.OSM('maps/pardubice.pbf')
walk_n, walk_e = osm.get_network(network_type='walking', nodes=True)
pub_n, pub_e = osm.get_network(network_type='driving+service', nodes=True)

walk_graph = osm.to_graph(walk_n, walk_e, graph_type="networkx")
pub_graph = osm.to_graph(pub_n, pub_e, graph_type="networkx")


# Thanks unknown student for making this key static :)))))))
# :)))))))))))))))))))))))))))))))))))))))))))))))))))))))))
DPMP_APIKEY = "3e86570d-56a1-4ec1-8012-c1a9f98d18cc"


def index(req):
    return render(req, 'index.html')


def search(req):
    _from = req.POST.get('from')
    _to = req.POST.get('to')
    _walk_speed = req.POST.get('walk_speed')
    _urgency = req.POST.get('urge')

    _bus_snapshot = get_buses(DPMP_APIKEY)
    _networks = {walk_network, drive_network}
    _route = aStar(
        _networks,
        _from,
        _to,
        _bus_snapshot,
        _walk_speed,
        _urgency
    )

    _context = {
        'results': [
            {
                'segments': [
                ]
            },
            {
                'segments': [
                ]
            }
        ]
    }

    print(_from, _to)

    return render(req, '_results.html', _context)
