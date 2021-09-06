#  python for connecting with mongodb

import re
from pymongo import mongo_client

client = mongo_client.MongoClient(port=27017)
db = client.business

data = {"firstname": "Rakhi", "lastname": "Jain", "mobileno": 7038680983, "city": "Malkapur"}

db.mydata.insert_one(data)
