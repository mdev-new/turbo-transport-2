from functools import partial
from flask import Flask, request

import networkx as nx

from . import graph
from .misc.constants import KMH_TO_MS

G = graph.get_graph("graph.graphml")


app = Flask(__name__)

@app.route('', methods=['POST'])
def login():
    pass

@app.route('', methods=['POST'])
def register():
    pass

@app.route('/logout', methods=['POST'])
def logout():
    pass

@app.route('', methods=['POST'])
def last_searches():
    return {
        'id': 0,
        'source': 'Hlavni nadrazi',
        'destination': 'Strossova'
    }

@app.route('', methods=['POST'])
def all_stations():
    return G.nodes()

@app.route("/search", methods=['POST'])
def search():
    request_data = request.json

    source = request_data['from']
    target = request_data['to']
    walk_speed = float(request_data['walk_speed'])
    urgency = int(request_data['urge'])

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

    return {
        'results': [newpath],
        'query': f'z:{source} kam:{target} rychlost_chuze:{walk_speed} nutnost:{urgency}'
    }
