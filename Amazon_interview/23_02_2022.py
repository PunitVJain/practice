# python for inheriting the class variables in python.

class SampleOne:
    
    def __init__(self, name) -> None:
        self.name = name
    
    def myname(self):
        return "In class SampleOne, method myname."

class SampleTwo:
    
    def myname(self):
        return "In class SampleTwo, Method myname."


class Sample(SampleOne, SampleTwo):

    def __init__(self, name) -> None:
        super().__init__(name)
    
sam  =  Sample("Punit Jain")
print(SampleOne.myname(sam))




