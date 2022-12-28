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
