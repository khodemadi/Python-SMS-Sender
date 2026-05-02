import http.client
import json

conn = http.client.HTTPSConnection("api.sms-webservice.com")
payload = "{\r\n  \"ApiKey\": \"YourApiKey\",\r\n  \"Recipients\": [\r\n    {\r\n      \"Sender\": 5000,\r\n      \"Text\": \"YourSMSText\",\r\n      \"Destination\": 09123456789,\r\n      \"UserTraceId\": 0000\r\n    }\r\n  ]\r\n}"
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/V3/SendMultiple", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
