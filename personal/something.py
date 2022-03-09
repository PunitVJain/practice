#  class for Punit Jain

class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    @property
    def length(self):
        return self.length
    
    @length.setter
    def length(self, other):
        pass