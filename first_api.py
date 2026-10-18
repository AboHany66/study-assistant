import requests

response = requests.get("https://api.github.com/users/AboHany66")

print(response.status_code)

data = response.json()

print(data)

print(data.get('age'))