#  python Encapsulation.

#  to encapsulate the things

class Sample(object):

    def __init__(self,first_name,second_name) -> None:
        super().__init__()
        self.first_name = first_name
        self.second_name = second_name
    
    def location(self):
        return "Malkapur" +' '+self.first_name+' '+self.second_name

if __name__ == "__main__":
    sa = Sample("Punit","Jain")
    print(sa.location())

# ---------------------------------------------------------------------------



class SampleThree:
    
    def dirname(self):
        return __annotations__

sam =  SampleThree()
print(sam.dirname())
