# classed in python with example.

class Sample:

    def add(self):
        return 'IN ADD method of Sample'
    
class Example:

    def add(self, numone, numtwo):
        return numone + numtwo
    
class MyExample(Sample, Example):
    pass

myex = MyExample()
print(Example.add(myex, 2, 3))
print(Sample.add(myex))
        