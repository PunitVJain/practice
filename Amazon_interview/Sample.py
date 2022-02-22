#  Study plan for amazon
class SampleBase:
    def __init__(self, bone, btwo) -> None:
        self.bone = bone
        self.btwo = btwo
    
    def full_name(self):
        return "Punit" +" "+ "Jain"
    
class SampleOne(SampleBase):
    def __init__(self) -> None:
        super().__init__()
    
so =  SampleOne()