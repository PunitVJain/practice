#  link list in python.

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.link = None
    @classmethod
    def __repr__(cls) -> str:
        return f"Instance of class {cls.__name__}"

nd = Node(2)

print(nd)