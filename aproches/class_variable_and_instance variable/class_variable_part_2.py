

class SampleOne:

    __num = 0

    def __new__(cls):
        if cls.__num >= 2:
            raise Exception("Too many objs created.")
        cls.__num +=1
        return super(SampleOne, cls).__new__(cls)

    def __init__(self) -> None:
        pass


sam = SampleOne()
sam1 = SampleOne()
#sam2 = SampleOne()
#sam3 = SampleOne()

print(sam.__dict__)
print(sam1.__dict__)
#print(sam2.__dict__)
