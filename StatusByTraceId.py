import http.client
import json

conn = http.client.HTTPSConnection("api.sms-webservice.com")
payload = json.dumps({
  "ApiKey": "YourApiKey",
  "UserTraceIds": [
    0
  ]
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/V3/StatusByUserTraceId", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
