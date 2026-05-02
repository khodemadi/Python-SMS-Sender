import http.client

conn = http.client.HTTPSConnection("api.sms-webservice.com")
payload = 'ApiKey=YourApiKey'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/api/V3/TokenList", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
