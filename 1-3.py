import requests

r = requests.get("http://facebook.com")
print(r.status_code)
print(r.ok)
