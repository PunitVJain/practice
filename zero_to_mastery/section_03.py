# Python with  Punit Jain

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
            raise "Length can't be '-ve'."
        self._length = length
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise "Width can't be '-ve'."
        self._width = width
    
    def __repr__(self) -> str:
        return "Instance of Rectangle class."
    
if __name__ =="__main__":
    try:
        rec = Rectangle(10, 20)
        print(rec.length)
    except Exception as ERROR:
        print("Instance can't be created.", ERROR)
    
