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
