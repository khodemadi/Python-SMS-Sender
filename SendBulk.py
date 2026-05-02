import http.client

conn = http.client.HTTPSConnection("api.sms-webservice.com")
payload = 'ApiKey=YourApiKey&Text=YourSMSText&Sender=5000&Recipients=09123456789'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/api/V3/SendBulk", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
