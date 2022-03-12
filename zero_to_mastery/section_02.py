# Rectangle in Python.

class Rectangle:

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def __repr__(self) -> str:
        return "Instance of Rectangle."
    
    def __str__(self) -> str:
        return "Instance of Rectangle."
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        if length <=0:
            raise "The value can't be negative."
        self._length = length 
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <=0:
            raise "The value can't be negative."
        self._width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
if __name__ == "__main__":
    rec = Rectangle(22, 11)
    print(rec.area())