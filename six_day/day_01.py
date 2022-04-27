#  this is python with Punit Jain


class Rectangle(object):

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def __repr__(self) -> str:
        return "Instance of Rectangle."
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, length):
        if length <= 0:
            raise "Lenght can be '-ve'."
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
    
    def perimeter(self):
        return 2 * (self.lenght + self.width)

class Square:

    def __init__(self, side) -> None:
        self.side = side
    
    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, side):
        if side <= 0:
            raise "Side can't be '-ve'."
        self._side = side
    
    def __repr__(self) -> str:
        return "Instance of Square."
    
    def area(self):
        return self.side * self.side
    
class Shape(object):
    pass
    
    
if __name__ == "__main__":
    rec = Rectangle(10, 20)
    print(rec.area())
    print(rec)
    sq = Square(10)
    print(sq.area())
    