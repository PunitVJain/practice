#  link list in python.

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.link = None
    
class LinkList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    
