import http.client

conn = http.client.HTTPSConnection("api.sms-webservice.com")
payload = ''
headers = {}
conn.request("GET", "/api/V3/Send?ApiKey=YourApiKey&Text=YourSMSText&Sender=5000&Recipients=09123456789", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
