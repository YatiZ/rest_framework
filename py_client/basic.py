import requests

endpoint = "http://localhost:8000/api/"
get_response = requests.post(endpoint,json = {"title":"How To Love","content":"People for always make mistakes", "price": 1000})
print(get_response.json())