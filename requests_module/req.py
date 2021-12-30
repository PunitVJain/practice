# python module

import requests
from requests.api import post

url = "https://www.google.com/"

res = requests.get(url).text
print(res)

def find_data(url = url):
    try:
        res = requests.get(url).text
        return res
    except Exception as err:
        return {"status": False, "msg": "Failed", "Error": err}, 200
    
