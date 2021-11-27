# interview question for infosect.
# shift the elements of the list by rt
mylist = [10, 30, 20, 40, 50, 60, 70, 80, 90, 11]
rt = 4

def func(mylist, rt):
    mynlist = mylist[:rt]
    mylist = mylist[rt:] + mynlist
    return mylist
print(func(mylist, rt))

# write a function to check the addition of the two elements will be rt.

rt = 60

def afun(mylist, rt):
    mylist = [(mylist[iteam], mylist[value]) for iteam in range(len(mylist)) for value in range(iteam, len(mylist)) if mylist[iteam] != mylist[value] and mylist[iteam] + mylist[value] == rt]
    return mylist

print(afun(mylist, rt))

# learn python the hard way.

#  print() --> Printing the things.

# 
print("Punit Jain")
print('India')
name = "Punit Jain"
print(f'Love to be Programmer {name}')
print("Punit Jain", name)
print('Malkapur' +name)
print("Punit Jain")

# learn to create link list

class Node:

    def __init__(self, data= 0, nextnode= None) -> None:
        """
        As in link list nodes 
        """
        self.data = data
        self.nextnode = nextnode

class LinkList:

    def __init__(self) -> None:
        self.head = None

    def print_link_list(self):
        temp = self.head
        while temp:
            print(temp.data, "--> ", end="")
            temp = temp.nextnode



link_list = LinkList()
link_list.head = Node(1)
secondnode = Node(4)
thirdnode = Node(7)


link_list.head.nextnode = secondnode
secondnode.nextnode = thirdnode


link_list.print_link_list()

 