# python to read json data

import datetime
import json


#mylist =  json.dumps(data)
class Sample:
  
    def add_index_timestamp(self,data):
        ''' adds two key values to the json 
        '''
        ct = datetime.datetime.now()
        for iteam, value in enumerate(data):
            value["index"] = iteam
            value["date_time_stamp"] = ct
        return data
    
    def change_key(self, data, ckey, mkey):
        '''changes the key names in the json'''
        data = json.dumps(data)
        data = data.replace(ckey, mkey)           
        return json.loads(data)
                
    def read_json_file(self, file):
        '''reads the json file.'''
        with open(file, 'r+') as file:
            file = json.loads(file.read())
            return file

def main():
    '''main method to start the execution.'''
    sa_one = Sample()
    data = "/media/putwind/Card1/Movies/Desktop/Python Practic Programmes/Python_Study/practice/class_and_function/file.json"
    
    print("first requirement---->", sa_one.read_json_file(data))
    print("Second recuirement--->", sa_one.add_index_timestamp(sa_one.read_json_file(data)))
    print("Third Requirement--->", sa_one.change_key(sa_one.read_json_file(data),"location", "place"))

if __name__ == "__main__":
    main()