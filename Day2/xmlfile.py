import requests

data=requests.get("https://www.w3.org/People/mimasa/test/")
print(data.content)