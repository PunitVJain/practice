# class python

class SampleOne:
    @classmethod
    def __repr__(cls) -> str:
        return f"Instance of class {cls.__name__}"

    
# to modify the instance return by __repr__ in python.


sam = SampleOne()
print(sam)