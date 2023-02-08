import requests 

endpoint = "http://localhost:8000/api/products/"

get_response = request.get(endpoint)
print(get_response.json())