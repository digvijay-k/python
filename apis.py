import requests
import json
# r = requests.get('https://catfact.ninja/fact')
# print(r.status_code)
# print(r.text)
# print("hiiiii")
# print(r.json)


url = "http://preprod-omsaggregator.nyk00-int.network/omsApis/v1/orderList?orderSource=NYKAA_D&emailId=sagar.malhotra@nykaa.com&offset=10&currentPage=0&enableNonGroup=true"

payload={}
headers = {}
# C:\Users\digvijay.kumar\AppData\Roaming\Python\Python310\Scripts
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
j = response.text

y = json.loads(j)

# the result is a Python dictionary:
# print("data")
print(type(y["data"]))
print(y["data"])


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

# print(response.text)
data = json.loads(response.text)
print(type(data["data"][0]))
print(data["data"][0]["itemCancelled"])

