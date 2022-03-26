# Python with me.
#  instance of class containg int elements in the list.
class Sample:

    def __init__(self, lst) -> None:
        self.lst = lst
    
    @property
    def lst(self):
        return self._lst
    
    @lst.setter
    def lst(self, lst):
        for _ in lst:
            if type(_) != int:
                raise "The element in the array is not int."
        self._lst = lst
    
    def __repr__(self) -> str:
        return "Instance of Sample."
    
if __name__ == "__main__":
    sam = Sample([1, 2, 3])
    print(sam)
        
