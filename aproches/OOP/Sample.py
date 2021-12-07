#  super class of the other classes
#  learning inheritance in Python 
#  diagonal inheritance.

class Sample:

    def __init__(self, name, mobno):
        self.name = name
        self.mobno = mobno
    
    def myname(self):
        return "My Name is", self.name, "My Mobile Number is", self.mobno 
    
class Example(Sample):

    def __init__(self, name, mobno):
        super().__init__(name, mobno)

class ExampleTwo(Sample):

    def __init__(self, name, mobno):
        super().__init__(name, mobno)

class GerExample(Example, ExampleTwo):

    def __init__(self, name, mobno):
        super().__init__(name, mobno)
    
    def name_and_number(self):
        return super().myname(), super().mobno

gx = GerExample("Punit Jain", 9999999999)
print(gx.name_and_number())
