from django.shortcuts import render
from .functionality import get_buses

import pyrosm

osm = pyrosm.OSM('pardubice.pbf')
walk_network = osm.get_network(network_type='walking')
drive_network = osm.get_network(network_type='driving+service')

# Thanks unknown student for making this key static :)))))))
# :)))))))))))))))))))))))))))))))))))))))))))))))))))))))))
DPMP_APIKEY = "3e86570d-56a1-4ec1-8012-c1a9f98d18cc"

RADIUS = 500  # meters


def index(req):
    return render(req, 'index.html')


def search(req):
    _from = req.POST.get('from')
    _to = req.POST.get('to')

    _buses = get_buses(DPMP_APIKEY).json()

    print(_buses, type(_buses))

    return render(req, '_results.html', {
        'results': [
            {
                'segments': [
                    {
                        'routes': [

                        ]
                    }
                ]
            },
            {
                'segments': {

                }
            }
        ]
    })
