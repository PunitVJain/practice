# python module

import requests

url = "https://www.google.com/"

url_2 = "https://www.naukri.com/mnjuser/homepage"

res = requests.get(url_2).text
print(res)

def find_data(url = url):
    try:
        res = requests.get(url).text
        return res
    except Exception as err:
        return {"status": False, "msg": "Failed", "Error": err}, 200
    
