# class method in python

class Example:

    def __init__(self, value_one, value_two) -> None:
        self.value_one = value_one
        self.value_two = value_two

    @classmethod
    def cmethod(cls):
        return "Punit Jain"


ex = Example(10, 20)

print(Example.cmethod()) #  class method takes class as first param in the place of self.
# it takes first argument as class
# it is bound with the class , it can change the state of the class
# it will chnage the state of each instance.
#  can be accessed by class & instances.
# -===========================================================================
# static metho