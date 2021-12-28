# python module

import requests
from requests.api import post

url = "https://www.google.com/"

res = requests.get(url).text
print(res)
