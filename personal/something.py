#  class for Punit Jain

#  @property is usefull to getter & setter methods in Pythonic way.

class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, other):
        if other <= 0:
            raise "Values can't be Zero."
        self._length = other
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, other):
        if other <= 0:
            raise "Value can't be Zero."
        self._width = other


rec = Rectangle(10, 20)
rec.length = 100
rec.width = 200
print(rec.length, rec.width)
