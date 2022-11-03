import requests
import json
data=requests.get('https://api.github.com/')
mydata=json.loads(data.text)
print(mydata['hub_url'])