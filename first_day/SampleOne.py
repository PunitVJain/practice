# python 

from re import A


class SampleOne:

    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def full_name(self):
        return self.fname +" "+self.lname
    

so =  SampleOne("Punit", "Jain")
print(so.full_name())

#  pythonic way to solve the febonacii series in python generator

def febgen(num):
    a, b = 0, 1
    for iteam in range(num):
        yield a 
        a, b = b, a+b
np = febgen(10)
print(np.__next__())
print(np.__next__())
print(np.__next__())
print(np.__next__())
print(np.__next__())
    
