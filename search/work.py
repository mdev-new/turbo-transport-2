import requests

MAX_WALK_DISTANCE = 500  # meters


def aStar(models, start, goal, buses, walk_speed, urgency):
    pass


def get_buses(apikey):
    req = requests.request(
        "POST",
        'https://online.dpmp.cz/api/buses',
        json=('{"key":"' + apikey + '"}')
    )

    return req
