# public access modifiers
# by default all the member variables & member functions are defined
#  public in python.
#  the member functions & member variables 



class SampleToday:

    def __init__(self, first_name:str, last_name:str, mobno:str, address:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self._mobno = mobno
        self.__address = address 
    
    def full_name(self): # member function is accessible everywhere
        return self.first_name +" "+ self.last_name

    def _mobile_no(self): # member function is accessible in class & derived class
        return "+91"+ "-" + self._mobno
    
    def __complete_address(self): #  member function is accessible in class
        return self.__address + " India"
    
class SampleTomorrow(SampleToday):

    def __init__(self, first_name: str, last_name: str, mobno: str, address: str) -> None:
        super().__init__(first_name, last_name, mobno, address)
    

st2  = SampleTomorrow("Punit", "Jain", "8237914234", "wakad, Pune")
print(st2.full_name())
print(st2._mobile_no())
#print(st2.__complete_address()) # as the __complete_address() is not accessible this will through an error

    


    


    
