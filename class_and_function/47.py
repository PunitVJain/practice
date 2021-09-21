# python to read json data
import json
import datetime



#mylist =  json.dumps(data)
class Sample:
    
    def func_dct(self, data):
        ct = datetime.datetime.now()
        for iteam, value in enumerate(data):
            value["index"] = iteam
            value["date_time_stamp"] = ct
        return data

def main():
    data = [{"firstname":"Punit", "lastname":"Jain", "mobileno":"8237914234", "location":"Malkapur"},
            {"firstname":"Rakhi", "lastname":"Jain", "mobileno":"7038680983", "location":"Pune"},
            {"firstname":"Rekha", "lastname":"Jain", "mobileno":"9689353311", "location":"Mumbai"},
            {"firstname":"Shravani", "lastname":"Jain", "mobileno":"9768777787", "location":"Banglore"}]

    sa_one = Sample()
    print(sa_one.func_dct(data))

if __name__ == "__main__":
    main()