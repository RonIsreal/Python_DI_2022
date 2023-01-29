import requests

response = requests.get("https://api.chucknorris.io/")
print(response.status_code)
print(response.text)
print(response.json)
print(response.headers)
