import http.client

conn = http.client.HTTPSConnection("api.sms-webservice.com")
payload = 'ApiKey=YourApiKey&TemplateKey=YourPattern&Destination=09123456789&P1=Param1&P2=Param2&P3=Param3'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/api/V3/SendTokenMulti", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
