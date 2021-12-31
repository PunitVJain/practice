# class python

class SampleOne:
    @classmethod
    def __repr__(cls) -> str:
        return f"Instance of class {cls.__name__}"

    


sam = SampleOne()
print(sam)