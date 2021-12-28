# python module

import requests

url = "https://www.google.com/"

res = requests.get(url).headers
print(res)