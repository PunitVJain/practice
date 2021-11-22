# python link list.

class LinkListNode:
    def __init__(self, data):
        self.data= data 
        self.nextnode = None

class LinkList:

    def createlinklist(self, data):
        return LinkListNode(data)
    
ll = LinkList()
print(ll.createlinklist(10))


