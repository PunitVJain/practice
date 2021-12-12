# python for Punit Jain

# how python works.

class linklistnode:
    
    def __init__(self, value, nextnode=None) -> None:
        self.data = value
        self.nextnode = nextnode

#  -----------------------------------------------------

# You are asked to ensure that the first and last names of people begin 
# with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.

mystr = "hello   world  lol"
def myfunc(mystr):
    mylist = mystr.split()
    mylist = list(map(lambda ele: ele.capitalize(), mylist))
    return " ".join(mylist)
print(myfunc(mystr))
