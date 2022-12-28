import requests
import json

req = requests.get('https://catfact.ninja/fact')
statuscode = req.status_code
def testCalculation():

    print(req.status_code)
    # print(r.text)
    # print(r.json)
    assert statuscode == 200
    # assert 2+2 == 4


def checkapi():
    r = requests.get('https://catfact.ninja/fact')
    # print(r.status_code)
    # print(r.text)
    # print(r.json)
    assert r.status_code == 200



