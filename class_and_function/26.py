#  OOP in Python.

class Dog:
    # class of the flask.
    def __init__(self, name: str) -> str:
        self.name = name

    def bark(self):
        # method of the Dog class.
        return ('bark......')
    
dog = Dog("Punit")
print(dog.bark())
