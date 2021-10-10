#  python is the best to work for Data structure & algorithms
# implementing tree data structure in python.
#  initially needed to create the node data type


class Node:

    def __init__(self, value) -> None:
        self.left = None
        self.data = value
        self.right = None
    
class Tree:

    def createnode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createnode(data)
        elif data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    
    def traversal_inorder(self, node):
        if node is not None:
            self.traversal_inorder(node.left)
            print(node.data, end='')
            self.traversal_inorder(node.right)
    
    def traversal_preorder(self, node):
        if node is not None:
            print(node.data, end='')
            self.traversal_inorder(node.left)
            self.traversal_inorder(node.right)
        

    

tree = Tree()
mylist = [5, 2, 3, 4, 5, 8, 3, 7, 8, 9, 10]
root = tree.createnode(mylist[0])
for iteam in range(1, len(mylist)):
    tree.insert(root, mylist[iteam])
print("Inorder---->")
tree.traversal_inorder(root)
print("Preorder---->")
tree.traversal_preorder(root)
print()
    

