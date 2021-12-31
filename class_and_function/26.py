#  OOP in Python.

class Dog:
    # class of the flask.
    def __init__(self, name: str) -> str:
        self.name = name
        # attribute of the class  'self'


    def bark(self):
        # method of the Dog class.
        return ('bark......')
    
dog = Dog("Punit")

cat = Dog("Jain")
