# python to read json data
import json
import datetime



#mylist =  json.dumps(data)
class Sample:
    data = [{"firstname":"Punit", "lastname":"Jain", "mobileno":"8237914234", "location":"Malkapur"},
            {"firstname":"Rakhi", "lastname":"Jain", "mobileno":"7038680983", "location":"Pune"},
            {"firstname":"Rekha", "lastname":"Jain", "mobileno":"9689353311", "location":"Mumbai"},
            {"firstname":"Shravani", "lastname":"Jain", "mobileno":"9768777787", "location":"Banglore"}]

    def func_dct(data):
        ct = datetime.datetime.now()
        for iteam, value in enumerate(data):
            value["index"] = iteam
            value["date_time_stamp"] = ct
        return data


