#  multiple inheritance in python.

class SampleOne:

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        return self.first_name + " " + self.last_name
    
class SampleTwo:

    def __init__(self, address) -> None:
        self.address = address
    
    def full_address(self):
        return self.address
    
class SampleThree:

    def __init__(self, mobile_no:int) -> None:
        self.mobile_no = mobile_no
    
    @property
    def mobile_no(self):
        return self._mobile_no
    
    @mobile_no.setter
    def mobile_no(self, mobile_no):
        if type(mobile_no) != int and str(mobile_no) != 10:
            raise "Mobile No is invalid."
        self._mobile_no = mobile_no

    def full_mobile_no(self):
        return self.mobile_no
    

