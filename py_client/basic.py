import requests

# endpoint = "hhttps://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"


get_response =requests.get(endpoint,json={'query':"hello world"}) # HTTP Request
#print(get_response.text) # print raw text code
print(get_response.json())
# print(get_response.status_code)
