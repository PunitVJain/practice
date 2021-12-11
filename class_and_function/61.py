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
    
    def __init__(self, first_name, last_name, mobile_no) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_num = mobile_no
    
    def full_name(self):
        return self.first_name + " " + self.last_name

    def mobile_no(self):
        return 

class SampleTwo(SampleOne):

    def __init__(self, first_name, last_name, mobile_no) -> None:
        super().__init__(first_name, last_name, mobile_no)
    
sam_two = SampleTwo("Punit", "Jain","9876543298") 
print(sam_two.full_name())#  inharited super class method 
print(sam_two.first_variable) #  class varibale accessed by the child class.








