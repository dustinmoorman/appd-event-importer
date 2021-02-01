import json, requests

apiKeyFile = open("apiKey.txt", "r")
accountNameFile = open("accountName.txt", "r")
apiKey = apiKeyFile.read().strip()
accountName = accountNameFile.read().strip()

print("Using Account Name: ", accountName)
print("Using API Key: ", apiKey)

##
# Set your schema name
##
schemaName = "dmoorman_demo"

url = "https://analytics.api.appdynamics.com/events/schema/" + schemaName

print("Using Schema Name: ", schemaName)

headerdata = {'X-Events-API-AccountName': accountName, 'X-Events-API-Key': apiKey, 'Content-Type': 'application/vnd.appd.events+json;v=2', 'Accept': 'application/vnd.appd.events+json;v=2'}

##
# Supported Types:
#
# - String
# - Date (ISO 8601)
# - Boolean
# - Integer
# - Float
#
# Note: You will also get two fields out of the box - pickupTimestamp and Timestamp.
# For more information: https://docs.appdynamics.com/display/PRO45/Analytics+Events+API
##

schema = '{"schema": {"URL": "string", "Type": "string", "Result": "boolean"}}'

response = requests.post(url, data = schema, headers = headerdata)

print("Status Code on Schema Create: ", response.status_code)
