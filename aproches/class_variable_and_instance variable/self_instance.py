#  self in python


class FirstSample:
    _num = 10
    """
    to scrap data
    """
    def __init__(self, name) -> None:
        """scrap data
        """
        self.name = name

    #  self is the instance of the class in python 
    #  which bind the arguments with instalce variable.


FS =  FirstSample("Punit")
print(FS)

