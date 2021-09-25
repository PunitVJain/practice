# python to read json data

import datetime
import json


#mylist =  json.dumps(data)
class Sample:
  
    def add_index_timestamp(self,data):
        ct = datetime.datetime.now()
        for iteam, value in enumerate(data):
            value["index"] = iteam
            value["date_time_stamp"] = ct
        return data
    
    def change_key(self, data):
        pass
    
    def read_json_file(self, file):
        with open(file, 'r+') as file:
            file = json.loads(file.read())
            return file

def main():
    data = "/media/putwind/Card1/Movies/Desktop/Python Practic Programmes/Python_Study/practice/class_and_function/file.json"

    sa_one = Sample()
    print(sa_one.add_index_timestamp(sa_one.read_json_file(data)))

if __name__ == "__main__":
    main()