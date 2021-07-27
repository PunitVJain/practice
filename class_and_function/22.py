#  python basics data-types in python.
# mystr = "Indian Army" --> string in python.s
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'P', 'u', 'n', 'i', 't'] --> list in python.
# mydict = {'First': 'Punit', 'Last': 'Jain'} --> Dictionary in python. 
# myset = {2, 4, 6, 8, 10} --> set in python
# mytup = (1, 2, 3, 4, 5, 6, 7, 8, 9) -- > tuple in python. 
# obool  = True --> boolen value.
# int & float --> number type.
#  complex numbers.
#  FUNCTIONS of the data-types in python.
# 1. String functions:- 
class Example:

    def initcaps(self, mystr):
        '''
        Converts the string in the initcaps.
        '''
        cap_str =  mystr.capitalize()
        return cap_str

    def upper_str(self, mystr):
        pass

    def main(self):
        ex = Example()
        mystr = input("Enter the string: ")
        print(ex.initcaps(mystr))


if __name__ == '__main__':
    exa = Example()
    exa.main()
