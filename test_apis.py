import requests
import json

r = requests.get('https://catfact.ninja/fact')
statuscode = r.status_code


def test_statusCode():
    # print(r.status_code)
    # print(r.text)
    # print(r.json)
    assert r.status_code == 200



