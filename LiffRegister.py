import requests, json

# Input Data
clientid = input("Client ID : ")
channelsecret = input("Channel Secret : ")
type = input("Type (full/compact/tall): ")
url = input("URL (SSL): ")

#Phase 1 (Get AuthToken)
host = "https://api.line.me/v2/oauth/accessToken"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    }
data = {
    "grant_type": "client_credentials",
    "client_id": clientid,
    "client_secret": channelsecret
    }
req = requests.post(host, data=data, headers=headers)
result = json.loads(req.text)
authToken = result["access_token"]

#Phase2 (Register Liff App)
host = "https://api.line.me/liff/v1/apps"
headers = {
    "Authorization": "Bearer " + authToken,
    "Content-Type": "application/json"
}
data = {
    "view": {
        "type": type,
        "url": url
    }
}
req = requests.post(host, json=data, headers=headers)
result = json.loads(req.text)
liffid = result["liffId"]
print ("Your Liff App : line://app/" + liffid)
