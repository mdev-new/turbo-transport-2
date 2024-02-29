import requests

def get_buses(apikey):
    req = requests.request(
        "POST",
        'https://online.dpmp.cz/api/buses',
        json='{"key":"3e86570d-56a1-4ec1-8012-c1a9f98d18cc"}'
    )

    return req
