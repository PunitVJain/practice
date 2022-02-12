#  python for Punit Jain
#  get ready to CISCO
class Sample:

    def fname(self):
        return "In Sample fname"

class SampleOne(Sample):

    def fname(self):
        return "In SampleOne fname"
    
class SampleTwo(SampleOne):

    def fname(self):
        return "In SampleTwo fname"

st = SampleTwo()
print(super(SampleOne, st).fname())


# trying to understand the concepts of OOP in python.

