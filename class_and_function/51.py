#  file modification

import json, datetime


class Example:

    def __init__(self, file_loc) -> None:
        self.file_loc = file_loc

    def read_file(self):
        with open(self.file_loc, "r+") as file:
            data  = json.loads(file.read())
            return data

    def add_fields_file(self, data):
        ct = datetime.datetime.now()
        for iteam, value in enumerate(data):
            value["index"] = iteam
            value["date_time_stamp"] = ct
        return data


def main():
    file_loc = "/media/putwind/Card1/Movies/Desktop/Python Practic Programmes/Python_Study/practice/class_and_function/file.json"
    Ex_one = Example(file_loc)
    print("First Requirement", Ex_one.read_file())
    print("Second Requirement", Ex_one.add_fields_file(Ex_one.read_file()))
    
if __name__ == "__main__":
    main()
