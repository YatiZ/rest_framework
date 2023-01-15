import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title':'Harry Potter',
    'content':'',
    'price':34
}

get_response = requests.post(endpoint,json=data)
print(get_response.json())