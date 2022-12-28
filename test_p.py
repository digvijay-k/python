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


def test_checkapi():
    r = requests.get('https://catfact.ninja/fact')
    # print(r.status_code)
    # print(r.text)
    # print(r.json)
    assert r.status_code == 200

url = "http://preprod-omsagg.nykfashion-int.net/omsApis/cancelOrderItem"

payload = json.dumps({
  "cancelItems": [
    {
      "comment": "testing",
      "reason": "Product is damage",
      "emailId": "8382841776@nykaafashion.com",
      "itemName": "DailyObjects Silver Metallic Fatty Tote Bag",
      "mobileNumber": "8382841776",
      "orderId": "NYK-83821-7750274",
      "itemQty": 1,
      "lineNo": 1,
      "sku": "NYFDAIOB00628"
    },
    {
      "comment": "testing",
      "reason": "Product is damage",
      "emailId": "8382841776@nykaafashion.com",
      "itemName": "DailyObjects Silver Metallic Fatty Tote Bag",
      "mobileNumber": "8382841776",
      "orderId": "NYK-83821-7750274",
      "itemQty": 1,
      "lineNo": 2,
      "sku": "NYFDAIOB00627"
    }
  ],
  "domain": "NYKAA_FASHION"
})
headers = {
  'Content-Type': 'application/json',
  'userType': 'user',
  'userEmail': '8382841776@nykaafashion.com'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
data = json.loads(response.text)

def test_cancelitem():
    assert response.status_code == 200

    assert data["data"][0]["itemCancelled"] == False





