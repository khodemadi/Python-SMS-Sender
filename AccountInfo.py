import http.client

conn = http.client.HTTPSConnection("api.sms-webservice.com")
payload = ''
headers = {
  'ApiKey': 'YourApiKey'
}
conn.request("POST", "/api/V3/AccountInfo", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
