from typing import TypedDict
import os
import networkx as nx

from .misc import utils

from .providers import (
    DpmpDataProvider,
    PedestrianDataProvider,
    IredoDataProvider,
    TransportMethod
)

# UNITS:
#  Time: Seconds
#  Distance: Meters
#  Speed: m/s


data_providers = {
    'dpmp': DpmpDataProvider("3e86570d-56a1-4ec1-8012-c1a9f98d18cc"),
    'iredo': IredoDataProvider(),
    'pedestrian': PedestrianDataProvider(50.046320731020536, 50.01764577632251, 15.741522692054847, 15.810664404535617,
                                         '["type"!="multipolygon"]["access"!="private"]["highway"~"footway|path|pedestrian|service|residential|living_street|steps|sidewalk|track|cycleway"]')
}


def get_delta(current_wt, distance, edge):
    edge_time_len = 0  # seconds
    departure_time = 0
    wait_time = 0
    delay = 0
    delta = (departure_time + wait_time + edge_time_len + delay) - current_wt
    weight = delta / distance  # unit: seconds/meter
    return weight, delta


def is_conn_viable(delta: int) -> bool:
    return delta >= 0

class Parameters(TypedDict):
    walk_speed: float
    cycle_speed: float


def edge_weight(params: Parameters, n1, n2, edge, current_weight):
    d_weight: int | None = None  # let's start with no connection
    if edge['method'] == TransportMethod.FOOT:
        d_weight = edge['length'] / params['walk_speed']
    elif edge['method'] == TransportMethod.BIKE:
        d_weight = edge['length'] / params['cycle_speed']
    else:
        # Here actually straight line distance benefits us
        # since the bus can go on a really long & slow round trip
        # and not move us anywhere
        distance_between = utils.haversine(n1['lat'], n1['lon'], n2['lat'], n2['lon'])
        d_weight, d_time = get_delta(current_weight, distance_between, edge)

    return d_weight if is_conn_viable(d_weight) else None


def get_graph(filename):

    # if not os.path.isfile(filename):
    graphs = [
        p.get_graph(p_name) for p_name, p in data_providers.items()
    ]

    G = nx.compose_all(graphs)

    nx.write_graphml(G, filename)

    # else:
    #     G = nx.read_graphml(filename, force_multigraph=True)

    assert G is not None, "No graph!"
    return G
