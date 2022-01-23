#  class in python 

class SampleFirst:

    def __init__(self) -> None:
        pass

    def add(self, one, two):
        return self.__add__(one, two)
    
sf = SampleFirst()
#sprint(sf.__hash__())

class SampleSecond:

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        pass


class Solution:

    def __init__(self,fname, lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def fullname(self):
        return self.fname + self.lname
    

solone =  Solution("Punit ", "Jain")
soltwo = Solution("Ram ", "Jain")
print(solone.fullname())
print(soltwo.fullname())



