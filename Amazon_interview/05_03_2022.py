# LinkList in Python.

class Node:
    
    def __init__(self, val) -> None:
        self.data = val
        self.next = None
    

class LinkList:

    def __init__(self) -> None:
        self.head = None
    
    def print_link_list(self):
        temp = self.head
        while temp:
            print(temp.data, end='--> ')
            temp = temp.next
        print()


ll = LinkList()
ll.head = Node(11)
second = Node(22)
third = Node(33)

ll.head.next = second
second.next = third
third.next = None

ll.print_link_list()

# ------------------------------------------------------------

#  what is recurretion in python?
# The function which calls itself is 

# ------------------------------------------------------------

# Python for inheritance


class SampleOne:

    def full_name(self):
        return "Punit Jain."

class SampleTwo:

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    

class Sample(SampleTwo):

    pass

sam = Sample('Punit', 'Jain')
print(SampleTwo.full_name(sam))