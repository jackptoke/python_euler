import requests
import json

api_key = 'AJsjqihWITOToUrXoxDSuCVi7GGTYcUj'
url = f"https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={api_key}"
# headers = {'Accept': 'svc/books/v3'}
r = requests.get(url)
response_dict = r.json()

readable_file = 'data/readable_nyt_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
# print(response_dict)
