import requests

endpoint = "http://localhost:8000/comment/"

get_response = requests.get(endpoint, json={"query":"Hello World"})

print(get_response.json())