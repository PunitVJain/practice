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

