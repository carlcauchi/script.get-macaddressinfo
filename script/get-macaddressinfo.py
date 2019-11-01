# load required modules
import argparse
import requests
import json

parser = argparse.ArgumentParser()
# mac example: 10-C3-7B-6C-C8-12
parser.add_argument("--mac", "-m", help="set mac address to be searched")
args = parser.parse_args()
if args.mac:
    macAddress = args.mac
print(args.mac)

# load Config file
with open("../config/app.config") as jsonConfigFile:
    appConfig = json.load(jsonConfigFile)

# set Variables to Config values
apiKey = appConfig.get("apiKey")
apiEndpoint = appConfig.get("apiEndpoint")

response = requests.get(apiEndpoint, params="apiKey=" + apiKey + "&output=json&search=" + macAddress)
responseJson = json.loads(response.text)

print("-------------------------------------------")
print("MAC Address Searched: " + macAddress)
print("Company Name: " + responseJson.get("vendorDetails").get("companyName"))
print("-------------------------------------------")