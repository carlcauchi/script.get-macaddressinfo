# 10-C3-7B-6C-C8-12
import requests
import json

apiEndpoint = "https://api.macaddress.io/v1"
apiKey = "at_FEwDD6vw3azLYrXNhrRxtxtdhl1tc"
macAddress = input("Please type the MAC Address to Search: ")

response = requests.get(apiEndpoint, params="apiKey=" + apiKey + "&output=json&search=" + macAddress)
responseJson = json.loads(response.text)

print("-------------------------------------------")
print("MAC Address Searched: " + macAddress)
print("Company Name: " + responseJson.get("vendorDetails").get("companyName"))
print("-------------------------------------------")