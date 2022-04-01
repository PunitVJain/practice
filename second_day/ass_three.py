# class In python

class Rectangle:

    def __init__(self) -> None:
        pass


class Cube(object):

    def __init__(self, side):
        self.side = side
    
    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, side):
        if side <=0:
            raise "Side can't be '-ve'."
        self._side = side
    
    def __repr__(self) -> str:
        return "Instance of class 'Cube'."
    
if __name__ == "__main__":
    cub = Cube(10)
    print(cub)
    