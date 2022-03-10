#python for @property decorator in python.

class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        if length <= 0:
            raise "Check the Assigned Value"
        self._length = length
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise "Check the Assigned Value"
        self._width = width
    
rac = Rectangle(10, 20)
print(rac.length)