# classes in python.
class Sample:

    def ffunc(self):
        return 'Punit Jain'
sobj = Sample()


# __________________________________________


# mulltiple inheritance in python.  


class SampleOne:
    
    def __init__(self, fname) -> None:
        self.fname = fname
    
    def loc(self):
        return "Malkapur"

class SampleTwo:

    def __init__(self, mname) -> None:
        self.mname = mname
    
    def loc(self):
        return "Pune"

class SampleThree:

    def __init__(self, lname) -> None:
        self.lname = lname
    
    def loc(self):
        return "Mumbai"

class Solution(SampleOne, SampleTwo, SampleThree):
    pass