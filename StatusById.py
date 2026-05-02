import http.client
import json

conn = http.client.HTTPSConnection("api.sms-webservice.com")
payload = json.dumps({
  "ApiKey": "YourApiKey",
  "Ids": [
    0
  ]
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/V3/StatusById", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
