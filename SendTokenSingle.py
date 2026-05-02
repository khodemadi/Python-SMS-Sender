import http.client

conn = http.client.HTTPSConnection("api.sms-webservice.com")
payload = ''
headers = {
  'ApiKey': 'YourApiKey',
  'TemplateKey': 'YourPattern',
  'Destination': '09123456789',
  'P1': 'Param1',
  'P2': 'Param2',
  'P3': 'Param3'
}
conn.request("GET", "/api/V3/SendTokenSingle", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
