#  python for amazon

class Sample:
    def __init__(self):
        pass
    def name(self):
        return "In Sample method is name."

class SampleOne(Sample):
    def __init__(self):
        super().__init__()
    def name(self):
        '''
        Method Overidden.
        '''
        print(Sample().name())
        return "In SampleOne Method is name."

#so = SampleOne()
#print(so.name())



class SampleTwo(Sample):

    def __init__(self):
        super().__init__()


st = SampleTwo()
print(Sample.name(st))
