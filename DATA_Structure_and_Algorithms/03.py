# python link list.

class LinkListNode:
    def __init__(self, data, nextnode = None):
        self.data= data 
        self.nextnode = nextnode

class LinkList:

    def createlinklist(self, data):
        return LinkListNode(data)
    
ll = LinkList()
print(ll.createlinklist(10))


