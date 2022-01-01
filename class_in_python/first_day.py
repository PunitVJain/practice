#  class in python 

class SampleFirst:

    def __init__(self) -> None:
        pass

    def add(self, one, two):
        return self.__add__(one, two)
    
sf = SampleFirst()
print(sf.__hash__())