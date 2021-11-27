# classes in python.
class Sample:
    """
    checking the how to create object in python 
    & access the methods of the class
    """
    def ffunc(self):
        return 'Sample Data'
sobj = Sample()

print(sobj.ffunc())

# first day with learn python the hard way.
#  how to get the version of the python by code.

import platform
print(platform.python_version())


# leet code .

#  create link list data structure in python.

class Node:

    def __init__(self, data = 0, next = None) -> None:
        """
        Node class will create Node data with next node address.
        by default data will be something & next will be None.
        """
        self.data = data
        self.next = next

class LinkList:

    def __init__(self) -> None:
        self.head = None
    
    def print_link_list(self):
        """ 
        Mothod will check head element is not empty 
        with the first attemp then next will be assigned 
        to the variable to check next element is not empty
        """
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

LinkLst =  LinkList()

LinkLst.head = Node(1)
second = Node(2)
third  = Node(3)

LinkLst.head.next = second

second.next = third

LinkLst.print_link_list()



