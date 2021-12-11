#  Python for Punit Jain.

# 

class Sample(object):

    def __init__(self) -> None:
        super().__init__()
    
    def myname(self):
        pass
#  python follows inheritance.
#  when the super class is inherited in call
#  in the consructor by default arguments are inherited.

#  inheritance of he class variable


class SampleOne:

    first_variable = "First Variable"
    
    def __init__(self, name) -> None:
        self.name = name

class SampleTwo(SampleOne):

    def __init__(self, name) -> None:
        super().__init__(name)
    
sam_one = SampleOne("First Instance Variable")

print(sam_one.first_variable)
