#  class 

class Rectangle(object):

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def __repr__(self) -> str:
        return "Instance of class Rectangle."
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        if length <= 0:
            raise "Lenght can't be '-ve'."
        self._length = length
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise "Width can't be '-ve'."
        self._width = width
    
    def area(self):
        return self.length * self.width
    
    def peremeter(self):
        return 2 * (self.length + self.width)

if __name__ == "__main__":
    rec = Rectangle(10, 20)
    print(rec.area())
    