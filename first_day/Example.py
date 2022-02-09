#  python with Punit Jain for CISCO
from tkinter.messagebox import NO


class Example:

    def __init__(self, name) -> None:
        self.name = name
        self.mobile_no = None
#  ========================================

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree:

    def create_tree(self):
        nd =  Node(5)
        return nd

tr =  Tree()
print(tr.create_tree())