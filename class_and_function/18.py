#  OOP in python.
#  python support all the procedures.


class Sample(object):

    def __init__(self) -> None:
        super().__init__()
    
    def rev_str(self, mystr):
        str_len = len(mystr)
        mylist = []
        while str_len:
            str_len -= 1
            mylist.append(mystr[str_len])
        return ''.join(mylist)


            

sam = Sample()
mystr = input("Enter the string to be reversed: ")
print(sam.rev_str(mystr))
