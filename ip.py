import requests

api_url = "https://api.ipify.org"
d = {"format": "json"}
response = requests.get(api_url, params=d)
r = response.json()
ip = r["ip"]
print(ip)

api_url1 = "https://geo.ipify.org/api/v1?apiKey=at_uNVGBgHXQhjKvsnqeVjme5ZVvQHww&ipAddress=8.8.8.8"
d1 = {"apiKey": "at_uNVGBgHXQhjKvsnqeVjme5ZVvQHww",\
      "ipAddress": ip}
response = requests.get(api_url1, params=d1)
r = response.json()
location = r["location"]
print(location)

